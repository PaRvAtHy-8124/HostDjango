from django.db import models

class Details(models.Model):
    Username=models.CharField(max_length=25)
    Email=models.EmailField()
    Password=models.CharField(max_length=10)

class Image_det(models.Model):
    Photo=models.ImageField(upload_to='media/',blank=True,null=True)
    Name=models.CharField(max_length=25)
    Brand=models.CharField(max_length=25)
    Price=models.IntegerField()