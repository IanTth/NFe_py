from django.shortcuts import render
import xml.etree.ElementTree as ET


# Create your views here.


def login(request):
    
    return render(request, 'index.html')

def register(request):

    return render(request, 'register.html')

def home(request):

    return render(request, 'home.html')

