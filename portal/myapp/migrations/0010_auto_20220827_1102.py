# Generated by Django 2.2.5 on 2022-08-27 11:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_skill_dateposted'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='field',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skill',
            name='dateposted',
            field=models.DateField(verbose_name=datetime.datetime(2022, 8, 27, 11, 1, 54, 345063, tzinfo=utc)),
        ),
    ]
