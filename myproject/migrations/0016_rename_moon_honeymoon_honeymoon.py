# Generated by Django 5.1.3 on 2024-11-21 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0015_honeymoon_delete_hony'),
    ]

    operations = [
        migrations.RenameField(
            model_name='honeymoon',
            old_name='moon',
            new_name='honeymoon',
        ),
    ]
