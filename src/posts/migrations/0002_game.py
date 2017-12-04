# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('year', models.TextField(blank=True)),
                ('igbd_url', models.URLField(blank=True)),
            ],
        ),
    ]
