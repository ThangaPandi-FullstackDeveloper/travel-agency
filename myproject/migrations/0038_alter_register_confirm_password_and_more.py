# Generated by Django 5.1.3 on 2024-11-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0037_delete_registration_rename_email_register_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Confirm_Password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='register',
            name='Password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='register',
            name='Phone_Number',
            field=models.IntegerField(max_length=128),
        ),
    ]
