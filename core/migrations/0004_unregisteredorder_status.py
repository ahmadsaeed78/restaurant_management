# Generated by Django 5.0.1 on 2024-11-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_table_is_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='unregisteredorder',
            name='status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('delivered', 'Delivered'), ('completed', 'Completed')], default='ordered', max_length=10),
        ),
    ]