# Generated by Django 5.0.3 on 2024-03-19 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('employees', '0004_alter_employee_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.employee')),
            ],
        ),
    ]
