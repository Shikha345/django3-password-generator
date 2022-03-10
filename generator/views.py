from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'hui43g6iu3o4'})

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    
    Charcters = list('abcdefghklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        Charcters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special'):
        Charcters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        Charcters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(Charcters)
    return render(request, 'generator/password.html', {'thepassword':thepassword})
