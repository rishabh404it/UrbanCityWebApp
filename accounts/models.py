from django.db import models

# Create your models here.
class Feedback(models.Model):
    Name = models.CharField(max_length=20)
    CityName = models.CharField(max_length=20)
    Img = models.ImageField(upload_to='pics')
    Desc = models.TextField()
    affectImg = models.ImageField(upload_to='pics')

    def __str__(self):
         return self.Name
    

     

   
