from django.shortcuts import render, redirect
from creator.models import Creator

# Create your views here.


def index(request):
    creators = Creator.objects.order_by('-id')[:3]
    if request.user.is_authenticated:
        try:
            creator = request.user.creator
        except Exception:
            return redirect("creator:edit")
    context = {
        'creator': creators
    }
    return render(request, "pages/index.html", context)
