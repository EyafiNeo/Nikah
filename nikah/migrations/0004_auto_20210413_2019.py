# Generated by Django 3.1.3 on 2021-04-13 14:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nikah', '0003_auto_20210413_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creatTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
