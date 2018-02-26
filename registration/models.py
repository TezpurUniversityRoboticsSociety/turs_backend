from django.db import models

# Create your models here.
class Student(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    name = models.CharField(max_length=140,blank=False)
    roll = models.CharField(max_length=8,blank=False)
    gender = models.CharField(max_length=6,choices=SEX,default='Others')
    course = models.CharField(max_length=20,blank=False)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(max_length=100,blank=False)
    thumb = models.ImageField(name='Photo',default='defaut.png',blank=True, null=True)
    id_card = models.ImageField(name='ID Card',default='defaut.png',blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name