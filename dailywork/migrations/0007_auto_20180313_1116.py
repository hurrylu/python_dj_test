# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-13 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailywork', '0006_auto_20180313_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='\u4ea7\u54c1ID'),
        ),
    ]
