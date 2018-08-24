from django.db import models
from django import forms
from .models import Member

# Create your models here.
class Form(forms.ModelForm):
    class Meta():
        model = Member
        fields = ['name','roll','gender','email','phone','course','photo','transaction_id']
