# Generated by Django 3.1.1 on 2020-11-18 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_profile_birth_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]