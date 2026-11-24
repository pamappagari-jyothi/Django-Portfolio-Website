from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Students App")

def about(request):
    return HttpResponse("About Students")

def contact(request):
    return HttpResponse("Contact Students")


