# Generated by Django 5.0.1 on 2024-11-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_table_unregisteredorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
