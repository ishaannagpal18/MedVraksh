# Generated by Django 3.1 on 2022-09-27 11:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0002_auto_20220927_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='otpmodel',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 27, 11, 49, 19, 508567, tzinfo=utc)),
        ),
    ]
