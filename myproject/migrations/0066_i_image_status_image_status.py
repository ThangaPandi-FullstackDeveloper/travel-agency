# Generated by Django 5.1.3 on 2024-12-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0065_i_image_delete_details1_details_place17_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='i_image',
            name='status',
            field=models.BooleanField(default=False, help_text='0-show,1-hidden'),
        ),
        migrations.AddField(
            model_name='image',
            name='status',
            field=models.BooleanField(default=False, help_text='0-show,1-hidden'),
        ),
    ]
