from django.shortcuts import render
from .models import Menu


def index(request):
    mendevil = Menu.objects.all()
    context = {
        "menus": mendevil
    }
    return render(request, "menu/main.html", context)


def menus(request):
    mendevil = Menu.objects.all()
    context = {
        "menus": mendevil
    }
    print(mendevil)
    return render(request, "menu/Menu.html", context)
def adres(request):
    return render(request, "menu/mbousosh.html", {})
