# Generated by Django 4.1.2 on 2022-11-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_myuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='phone'),
        ),
    ]
