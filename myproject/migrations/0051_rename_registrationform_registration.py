# Generated by Django 5.1.3 on 2024-11-25 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0050_rename_register_registrationform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegistrationForm',
            new_name='Registration',
        ),
    ]
