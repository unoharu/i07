# Generated by Django 3.2.19 on 2024-06-18 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_alter_table_max_seats_alter_table_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]