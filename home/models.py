from django.db import models

# Create your models here.
class Timeline(models.Model):
    date = models.DateField(blank=False)
    title = models.CharField(blank=False, max_length=30)
    event = models.TextField(blank=False)

    def __str__(self):
        return self.title