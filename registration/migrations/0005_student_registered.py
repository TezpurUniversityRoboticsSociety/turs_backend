# Generated by Django 2.0.2 on 2018-03-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20180223_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='registered',
            field=models.BooleanField(default=False),
        ),
    ]
