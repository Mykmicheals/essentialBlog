# Generated by Django 4.1.2 on 2022-10-21 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_post_description_alter_post_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdminPost',
        ),
    ]