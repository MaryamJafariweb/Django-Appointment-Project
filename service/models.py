from django.db import models


# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    title1 = models.CharField(max_length=100, blank=True, null=True)
    title2 = models.CharField(max_length=100, blank=True, null=True)
    title3 = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    image1 = models.ImageField(upload_to='images', blank=True, null=True)
    image2 = models.ImageField(upload_to='images', blank=True, null=True)
    image3 = models.ImageField(upload_to='images', blank=True, null=True)
    body = models.TextField()
    body1 = models.TextField(blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)

