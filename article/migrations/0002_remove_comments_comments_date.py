# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 12:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_date',
        ),
    ]
