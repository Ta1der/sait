from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="index"),
    path('menu', views.menus, name="menu"),
    path("adres", views.adres, name="adres")
]