# Generated by Django 5.0.3 on 2024-03-16 17:59

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('permission_department', models.CharField(max_length=50)),
                ('permission_employee', models.CharField(max_length=50)),
                ('permission_appointment', models.CharField(max_length=50)),
                ('permission_customer', models.CharField(max_length=50)),
            ],
        ),
    ]
