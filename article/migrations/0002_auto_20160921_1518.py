# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-21 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
