from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def project(request):
    return render(request,'project.html')

def navbar(request):
    return render(request,'navbar.html')


