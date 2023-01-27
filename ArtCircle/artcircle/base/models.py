from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Member(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    prn = models.CharField(max_length=20)
    phone = models.IntegerField(null=True, blank=True)
    joinDate = models.DateField(default=timezone.now)

    def __str__(self):
        return self.firstName


class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, null=True, blank=True)
    startTime = models.DateTimeField(default=timezone.now)
    endTime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
