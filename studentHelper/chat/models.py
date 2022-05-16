from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Questions
class question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ques_id=models.AutoField(primary_key=True)
    msg=models.TextField()

#Answered
class answer(models.Model):
    question=models.ForeignKey(question,on_delete=models.CASCADE)
    user_id=models.IntegerField(null=True)
    ans=models.TextField()
    