# Generated by Django 2.2.5 on 2022-08-27 12:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20220827_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='dateposted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]