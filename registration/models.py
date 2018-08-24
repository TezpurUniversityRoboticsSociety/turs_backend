from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.
class Member(models.Model):
    SEX = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    TYPE = [
        ('Executive Professor', 'Executive Professor'),
        ('Executive Member', 'Executive Member'),
        ('Member', 'Member'),
        ('Alumni', 'Alumni'),
    ]

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    

    name = models.CharField(max_length=140,blank=False)
    roll = models.CharField(max_length=8,blank=False)
    gender = models.CharField(max_length=6,choices=SEX,default='Others')
    course = models.CharField(max_length=25,blank=False)
    phone = models.IntegerField(blank=True,null=True)
    email = models.EmailField(max_length=100,blank=False)
    photo = models.ImageField(default='default.png',blank=False, null=True, validators=[validate_image])
    transaction_id = models.CharField(max_length=25,blank=False,default="NO Transaction ID provided")
    membership = models.CharField(max_length=20,choices=TYPE,default='Member')
    designation = models.CharField(max_length=30,default='Member')
    github = models.URLField(max_length=100,blank=True)
    facebook = models.URLField(max_length=100,blank=True)
    linkedin = models.URLField(max_length=100,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    registered = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name