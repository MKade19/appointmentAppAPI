# Generated by Django 5.0.3 on 2024-03-18 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
