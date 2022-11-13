import xml.etree.ElementTree as ET

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        return render(request, 'home.html')
        #email = request.POST.get('email')
        #password = request.POST.get('senha')

        #user = authenticate(email=email, password=password)


        


def register(request):

    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        password = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Usuário já existe')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse('usuário cadastrado')

def home(request):
    return render(request, 'home.html')
    #if request.user.is_authenticated:
        #return render(request, 'home.html')
    #else:
        #return HttpResponse('vc n esta logado')
    