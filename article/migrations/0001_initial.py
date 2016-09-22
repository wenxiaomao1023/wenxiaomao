# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-21 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
