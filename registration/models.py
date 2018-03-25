from django.db import models

# Create your models here.
class Student(models.Model):
    SEX = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    TYPE = [
        ('Teacher', 'Teacher'),
        ('Student Executive Member', 'Student Executive Member'),
        ('Member', 'Member'),
    ]
    name = models.CharField(max_length=140,blank=False)
    roll = models.CharField(max_length=8,blank=False)
    gender = models.CharField(max_length=6,choices=SEX,default='Others')
    course = models.CharField(max_length=20,blank=False)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(max_length=100,blank=False)
    photo = models.ImageField(default='defaut.png',blank=True, null=True)
    id_card = models.ImageField(default='defaut.png',blank=True, null=True)
    membership = models.CharField(max_length=20,choices=TYPE,default='Member')
    designation = models.CharField(max_length=20,default='Member')
    facebook = models.CharField(max_length=100,blank=True,default='#')
    github = models.CharField(max_length=100,blank=True,default='#')
    linkedin = models.CharField(max_length=100,blank=True,default='#')
    date = models.DateTimeField(auto_now_add=True)
    registered = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name