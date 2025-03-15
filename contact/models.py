from django.db import models


# Create your models here.
class Info(models.Model):
    phone1 = models.CharField(max_length=11, null=True, blank=True)
    phone2 = models.CharField(max_length=11, null=True, blank=True)
    phone3 = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField()
    email = models.EmailField()


class Contact(models.Model):
    full_name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    subject = models.CharField(max_length=300)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.full_name}-{self.created}'


