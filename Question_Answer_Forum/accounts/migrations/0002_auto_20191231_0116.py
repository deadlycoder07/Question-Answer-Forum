# Generated by Django 3.0.1 on 2019-12-30 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='user',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='user',
            name='width_field',
        ),
    ]
