# Generated by Django 3.2 on 2022-01-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immasin', '0006_auto_20220101_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide1',
            name='strength',
            field=models.IntegerField(default=0),
        ),
    ]
