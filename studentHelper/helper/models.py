import email
from operator import mod
from django.db import models
from django.contrib.auth.models import User
class UserData(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=25)
    collage_name=models.CharField(max_length=50)
    type=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    def __str__(self):
        return self.name