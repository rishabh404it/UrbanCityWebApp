from rest_framework import serializers
from .models import Feedback
from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer,HyperlinkedIdentityField


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    Img = serializers.ImageField(use_url=True)
    affectImg = serializers.ImageField(use_url=True)
    class Meta:
       model= Feedback
       fields=['url','Name','CityName','Img','Desc','affectImg']
