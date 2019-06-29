# Create your views here.
from django.shortcuts import render

def root(request):
    return render(request, 'first_app/tesla.html')

def pacman(request):
    return render(request, 'first_app/pacman.html')