from django.shortcuts import render
from .models import *
# Create your views here.

def sellerRegister(request):
    return render(request, 'register.html',{})