# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def show(request, my_val):
    return HttpResponse("placeholder to display blog number: " + str(my_val))

def edit(request, my_val):
    return HttpResponse("placeholder to edit blog: " + str(my_val))

def create(request):
    return redirect("/")

def destroy(request, my_val):
    return redirect("/")
