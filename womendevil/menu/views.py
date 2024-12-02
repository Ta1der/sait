from django.shortcuts import render
from .models import Menu


def index(request):
    men = Menu.objects.all()
    context = {
        "menus": men
    }
    return render(request, "menu/index.html", context)


def menus(request):
    return render(request, "menu/Menu.html", {})
