# Generated by Django 5.1.3 on 2024-12-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0067_international'),
    ]

    operations = [
        migrations.DeleteModel(
            name='International',
        ),
        migrations.RemoveField(
            model_name='i_image',
            name='place24',
        ),
        migrations.RemoveField(
            model_name='i_image',
            name='place25',
        ),
        migrations.RemoveField(
            model_name='i_image',
            name='place26',
        ),
        migrations.RemoveField(
            model_name='i_image',
            name='place27',
        ),
        migrations.RemoveField(
            model_name='i_image',
            name='place28',
        ),
        migrations.RemoveField(
            model_name='i_image',
            name='place29',
        ),
        migrations.RemoveField(
            model_name='i_image',
            name='place30',
        ),
        migrations.RemoveField(
            model_name='i_image',
            name='place31',
        ),
        migrations.AddField(
            model_name='i_image',
            name='i_Image_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='Image_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
