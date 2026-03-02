from django.urls import path
from .views import index
from django.shortcuts import render

def shopping(request):
    return render(request, "main/shopping.html")

urlpatterns = [
    path("", index, name="index"),
    path("shopping/", shopping, name="shopping"),
]