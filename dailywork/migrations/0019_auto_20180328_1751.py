# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-28 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailywork', '0018_auto_20180328_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='id',
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_id',
            field=models.IntegerField(help_text='\u8bf7\u8f93\u5165\u5458\u5de5\u5de5\u53f7\uff1a', primary_key=True, serialize=False, unique=True, verbose_name='\u5de5\u53f7'),
        ),
    ]
