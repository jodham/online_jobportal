# Generated by Django 2.2.5 on 2022-08-27 14:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20220827_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
