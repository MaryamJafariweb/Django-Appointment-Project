from django.db import models
from django.urls import reverse


# Create your models here.

class Education(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    image = models.ImageField(upload_to='education')
    short_description = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    offer = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    def get_absolute_url(self):
        return reverse('education_detail', args=[self.slug])


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name='comment')
