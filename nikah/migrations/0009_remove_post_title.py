# Generated by Django 3.1.3 on 2021-04-14 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nikah', '0008_auto_20210414_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]