# Generated by Django 2.0.2 on 2018-04-06 11:41

from django.db import migrations, models
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_auto_20180331_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='id_card',
        ),
        migrations.AlterField(
            model_name='member',
            name='course',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='member',
            name='designation',
            field=models.CharField(default='Member', max_length=30),
        ),
        migrations.AlterField(
            model_name='member',
            name='membership',
            field=models.CharField(choices=[('Executive Professor', 'Executive Professor'), ('Executive Member', 'Executive Member'), ('Member', 'Member'), ('Alumni', 'Alumni')], default='Member', max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(default='default.png', null=True, upload_to='', validators=[registration.models.Member.validate_image]),
        ),
    ]