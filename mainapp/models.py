

from django.db import models


# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=40,default=None)
    password = models.CharField(max_length=40)
