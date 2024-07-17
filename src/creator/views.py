from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Creator
from .forms import CreatorForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("creator:login")
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "pages/creator/signup.html", context)

@login_required
def mypage(request):
    creator = request.user.creator
    supports = creator.supports.filter(is_paid=True)
    total = 0
    for support in supports:
        total += support.amount
    context = {"creator": creator, "supports": supports, "total": total}
    return render(request, "pages/creator/mypage.html", context)


def creators(request):
    creators = Creator.objects.all()
    context = {"creators": creators}
    return render(request, "pages/creator/creators.html", context)

def creator(request, pk):
    creator = Creator.objects.get(pk=pk)
    context = {"creator": creator}
    return render(request, "pages/creator/creator.html", context)


def support_success(request, creator_id, support_id):
    support = Support.objects.get(pk=support_id)
    payment = Client.payment(PAYMENT_KEY, MARCHANT_UUID)
    result = payment.info(
        {"uuid": f"{support.cryptomus_uuid}", "order_id": f"{support.id}"}
    )
    if result["payment_status"] == "paid":
        support.is_paid = True
        support.save()
    return render(request, "pages/creator/success.html")


def edit(request):
    try:
        creator = request.user.creator
        if request.method == "POST":
            form = CreatorForm(request.POST, request.FILES, instance=creator)

            if form.is_valid():
                form.save()
                return redirect("app:index")
        else:
            form = CreatorForm(instance=creator)
    except Exception:
        if request.method == "POST":
            form = CreatorForm(request.POST, request.FILES)

            if form.is_valid():
                creator = form.save(commit=False)
                creator.user = request.user
                creator.save()
                return redirect("app:index")
        else:
            form = CreatorForm()
    context = {"form": form}
    return render(request, "pages/creator/edit.html", context)
