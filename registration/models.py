from django.db import models

# Create your models here.
class RegistrationForm(models.Model):
    name = models.CharField(max_length=140)
    roll = models.CharField(max_length=8)
    course = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name