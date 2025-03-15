from django.db import models
from django_jalali.db import models as jalali_model
from accounts.models import User


# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    slug = models.SlugField()
    image = models.ImageField(upload_to='blog_images')
    description = models.TextField()
    created = jalali_model.jDateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.CharField(max_length=30)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='post_comments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply_comments', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return f'{self.author}-{self.body[:20]}'

