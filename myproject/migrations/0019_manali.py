# Generated by Django 5.1.3 on 2024-11-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0018_shimla'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manali',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manali', models.ImageField(upload_to='pic')),
                ('plan', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
            ],
        ),
    ]
