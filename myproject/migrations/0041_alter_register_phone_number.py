# Generated by Django 5.1.3 on 2024-11-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0040_alter_register_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Phone_Number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
