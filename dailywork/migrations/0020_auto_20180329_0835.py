# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-29 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dailywork', '0019_auto_20180328_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produce',
            name='operator',
            field=models.ForeignKey(blank=True, help_text='\u8bf7\u9009\u62e9\u4f5c\u4e1a\u5458\uff1a', null=True, on_delete=django.db.models.deletion.CASCADE, to='dailywork.Worker'),
        ),
    ]