# Generated by Django 4.2.7 on 2024-04-11 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tsuka', '0002_alter_users_options_alter_users_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='users',
            name='lastname',
        ),
    ]
