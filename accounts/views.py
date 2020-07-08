from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth  
from .models import Feedback
from rest_framework import viewsets
from .serializers import FeedbackSerializer
from django_filters import FilterSet
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action 

# Create your views here.
def register(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
       
        if password1==password2:
            if len(password1 and password2) <= 5:
                messages.info(request,'Password must be of length greater than 5 digits')  
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken ')  
                return redirect('register')
            elif User.objects.filter(email=email).exists():  
                messages.info(request,'Email Already Taken !') 
                return redirect('register')
            else:
                  
               user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email,)
               
               return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')       
    else:
        return render(request, 'register.html')

def login(request):
        if request.method =='POST':
                   
            username=request.POST['username']
            password=request.POST['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request,'Username or Password not maching')    
                return redirect('login')
        else:
           return render(request, 'login.html')   

      
def logout(request):
    
    auth.logout(request)
    return redirect('/')

def issueinfo(request):
    if request.method =='POST':
       
        Name = request.POST['Name']
        CityName=request.POST['CityName']
        Img=request.POST['Img']   
        Desc=request.POST['Desc']
        affectImg = request.POST['affectImg']
                 
        problems=Feedback(Name=Name,CityName=CityName,Img=Img,Desc=Desc,affectImg=affectImg)
        problems.save()
        return render(request,'thanks.html')
    else:
        return render(request, 'feedback.html')    

class FeedbackFilter(filters.FilterSet):
    Name = filters.CharFilter('Name')
   

    class Meta:
        model = Feedback
        fields = ("Name","CityName")

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = (OrderingFilter,SearchFilter )
    search_fields = ('Name', 'CityName')
    ordering_fields = ('Name','CityName')
   
   
def accountinfo(request):
    return render(request,'profile.html')    

