# Generated by Django 5.1.3 on 2024-11-22 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0023_rename_kodaikannal_kodaikanal_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kodaikanal',
            new_name='Kodai',
        ),
        migrations.RenameField(
            model_name='kodai',
            old_name='Kodaikanal',
            new_name='Kodai',
        ),
    ]
