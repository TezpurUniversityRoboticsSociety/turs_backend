# Generated by Django 2.0.2 on 2018-03-30 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_auto_20180330_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
