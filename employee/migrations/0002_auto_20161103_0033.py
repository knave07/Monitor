# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.IntegerField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
