# Generated by Django 3.1.3 on 2021-04-16 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nikah', '0011_auto_20210414_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
    ]
