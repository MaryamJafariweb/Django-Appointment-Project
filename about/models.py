from django.db import models


# Create your models here.
class About(models.Model):
    description = models.TextField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()


class Comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='image', blank=True, null=True)
    body = models.TextField()
