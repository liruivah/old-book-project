from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    dept = models.CharField(max_length=15)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.username

admin.site.register(User)
