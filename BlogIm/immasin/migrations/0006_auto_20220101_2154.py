# Generated by Django 3.2 on 2022-01-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immasin', '0005_auto_20220101_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='strength',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='strength',
            field=models.IntegerField(default=0),
        ),
    ]