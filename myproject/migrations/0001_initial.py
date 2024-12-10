# Generated by Django 5.1.3 on 2024-11-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pic')),
                ('location', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
            ],
        ),
    ]
