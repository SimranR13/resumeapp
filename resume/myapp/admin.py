from resume.myapp.models import Message, message
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Message)