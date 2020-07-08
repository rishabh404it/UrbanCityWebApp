from django.shortcuts import render, redirect
from .models import Users


# Create your views here.

def index(request):
    dests=Users.objects.all() 
  
    return render(request,'index.html',{'dests': dests})

