# Generated by Django 3.1.4 on 2021-01-31 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20210105_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='blog',
            name='Created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
