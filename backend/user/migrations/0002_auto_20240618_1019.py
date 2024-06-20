# Generated by Django 3.2.19 on 2024-06-18 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='group_id',
        ),
        migrations.AddField(
            model_name='customer',
            name='people',
            field=models.IntegerField(blank=True, null=True, verbose_name='people'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
