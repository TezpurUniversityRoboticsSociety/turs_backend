# Generated by Django 2.0.2 on 2018-03-31 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_auto_20180331_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='facebook',
            field=models.URLField(blank=True, default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='github',
            field=models.URLField(blank=True, default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='linkedin',
            field=models.URLField(blank=True, default='#', max_length=100),
        ),
    ]