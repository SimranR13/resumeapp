from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=50),
    email = models.CharField(max_length=50),
    subject = models.CharField(max_length=100),
    message = models.TextField(max_length=1000),