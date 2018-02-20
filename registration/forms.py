from django.db import models
from django import forms
from .models import RegistrationForm

# Create your models here.
class Form(forms.Form):
    class Meta():
        model = RegistrationForm
        fields = ['name','roll','email','phone','course']

    def __str__(self):
        return self.name