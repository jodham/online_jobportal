# Generated by Django 2.2.5 on 2022-07-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20220722_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(default='default.png', null=True, upload_to='profilepics'),
        ),
    ]
