import json

from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from cryptomus import Client

from .models import Creator, Support


MERCHANT_UUID = settings.MERCHANT_UUID
PAYMENT_KEY = settings.PAYMENT_KEY


@csrf_exempt
def create_support(request):
    host = request.get_host()
    if request.method == "POST":
        creator = request.POST
        amount = request.POST.get("amount", "")
        email = request.POST.get("email", "")
        creator_id = request.POST.get("creator_id", "")

        # Create support

        support = Support.objects.create(
            creator_id=creator_id, amount=amount, email=email
        )

        # Talk to cryptomus

        data = {
            "amount": str(amount),
            "currency": "USD",
            "network": "Tron",
            "order_id": str(support.id),
            "url_return": f"https://{host}/creators/{creator_id}/",
            "url_success": f"https://{host}/creators/{creator_id}/success/{str(support.id)}/",
            "to_currency": "USDT",
        }

        payment = Client.payment(PAYMENT_KEY, MERCHANT_UUID)

        result = payment.create(data)
        if result["response_code"] == 200: 
            uuid = result["uuid"]
            url = result["url"]
            support.payment_uuid = uuid
            support.save()
            return JsonResponse({"uuid": uuid, "url": url})
        
        return JsonResponse(result["response_code"])
    else:
        return JsonResponse({"success": False})
