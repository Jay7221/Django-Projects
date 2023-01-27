from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, null = True, blank = True, on_delete=models.SET_NULL)
    title = models.CharField(max_length = 200, null = True)
    description = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User, null = True, blank = True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null = True, blank= True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    message = models.TextField(null = True, blank = True)
