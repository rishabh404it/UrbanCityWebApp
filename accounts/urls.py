from django.urls import path, include
from . import views
from accounts import views
from rest_framework import routers
from .models import Feedback



router = routers.DefaultRouter()
router.register('Feedback', views.FeedbackViewSet)


urlpatterns= [
    path('register', views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('issues_info',views.issueinfo,name='issues_info'),
    path('profile',views.accountinfo,name='profile'),
    path('api', include(router.urls),name='apiurl'),       
    ]

