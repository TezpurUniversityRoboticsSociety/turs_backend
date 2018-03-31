from django.db import models
from django.conf import settings
import os

# Create your models here.
class Member(models.Model):
    SEX = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    TYPE = [
        ('Executive Member', 'Executive Member'),
        ('Member', 'Member'),
        ('Alumni', 'Alumni'),
    ]
    name = models.CharField(max_length=140,blank=False)
    roll = models.CharField(max_length=8,blank=True)
    gender = models.CharField(max_length=6,choices=SEX,default='Others')
    course = models.CharField(max_length=20,blank=True)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(max_length=100,blank=False)
    photo = models.ImageField(default='default.png',blank=False, null=True)
    id_card = models.ImageField(default='default.png',blank=True, null=True)
    membership = models.CharField(max_length=20,choices=TYPE,default='Member')
    designation = models.CharField(max_length=20,default='Member')
    facebook = models.CharField(max_length=100,blank=True,default='#')
    github = models.CharField(max_length=100,blank=True,default='#')
    linkedin = models.CharField(max_length=100,blank=True,default='#')
    date = models.DateTimeField(auto_now_add=True)
    registered = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name