# Generated by Django 5.1.3 on 2024-11-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0013_europe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hony', models.ImageField(upload_to='pic')),
                ('plan', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
            ],
        ),
    ]
