from django.db import models
from django import forms
from .models import Student

# Create your models here.
class Form(forms.ModelForm):
    class Meta():
        model = Student
        fields = ['name','roll','gender','email','phone','course','Photo','ID Card']
