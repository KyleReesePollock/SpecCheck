# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20171204_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='igbd_url',
            new_name='url',
        ),
    ]
