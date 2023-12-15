from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, "index.html")

def logout(request):
    return render(request, "index.html")

