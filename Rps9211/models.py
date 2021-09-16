from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)

    Birthday = models.DateField(blank= True)
    Website =models.TextField(blank= True)
    Phone =models.IntegerField(max_length=12)
    Age =models.IntegerField()
    City = models.CharField(max_length=20)
    Degree = models.TextField(max_length=200)
    Freelance =models.TextField(max_length=20)

    def __str__(self):
        return self.user.username

class skills(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)

    skill =models.TextField(max_length=20)
    level =models.IntegerField(max_length=9)
    def __str__(self):
            return self.user.username


class Education(models.Model):
     user =models.ForeignKey(User,on_delete=models.CASCADE)
     Degree =models.TextField(max_length=200)
     year =models.IntegerField(max_length=9)
     college =models.TextField(max_length=60)
     def __str__(self):
       return self.user.username


