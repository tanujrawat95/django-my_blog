# Generated by Django 3.1.4 on 2021-01-31 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20210131_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
