# Generated by Django 3.2 on 2022-01-05 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immasin', '0010_auto_20220104_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='grop',
            field=models.CharField(choices=[('accessories', 'accessories'), ('pc', 'pc'), ('notebook', 'notebook'), ('mobile', 'mobile')], default='mobile', max_length=20),
        ),
    ]
