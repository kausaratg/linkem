# Generated by Django 4.2.3 on 2023-07-14 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_link', '0002_add_link_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_link',
            name='slug',
        ),
    ]
