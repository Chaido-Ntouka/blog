from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    date = models.DateTimeField(auto_now_add=True) 
    thumb = models.ImageField(default='default.jpg',blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

    def get_absolute_url(self):
        return reverse("detail", args=[self.id,self.self.slug])
    
