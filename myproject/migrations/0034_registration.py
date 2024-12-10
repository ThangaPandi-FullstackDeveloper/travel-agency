# Generated by Django 5.1.3 on 2024-11-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0033_image_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
