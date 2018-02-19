# Generated by Django 2.0.2 on 2018-02-19 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('roll', models.CharField(max_length=8)),
                ('course', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
