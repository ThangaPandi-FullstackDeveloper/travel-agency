# Generated by Django 5.1.3 on 2024-11-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0035_remove_registration_date_registered_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
