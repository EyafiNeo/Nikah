# Generated by Django 3.1.3 on 2021-04-14 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nikah', '0009_remove_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='details',
            field=models.TextField(default=' '),
        ),
    ]