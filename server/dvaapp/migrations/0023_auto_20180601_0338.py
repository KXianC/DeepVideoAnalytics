# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-01 03:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0022_auto_20180531_0820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regionlabel',
            name='event',
        ),
        migrations.RemoveField(
            model_name='regionlabel',
            name='frame',
        ),
        migrations.RemoveField(
            model_name='regionlabel',
            name='label',
        ),
        migrations.RemoveField(
            model_name='regionlabel',
            name='region',
        ),
        migrations.RemoveField(
            model_name='regionlabel',
            name='video',
        ),
        migrations.RemoveField(
            model_name='tubelabel',
            name='event',
        ),
        migrations.RemoveField(
            model_name='tubelabel',
            name='label',
        ),
        migrations.RemoveField(
            model_name='tubelabel',
            name='tube',
        ),
        migrations.RemoveField(
            model_name='tubelabel',
            name='video',
        ),
        migrations.DeleteModel(
            name='RegionLabel',
        ),
        migrations.DeleteModel(
            name='TubeLabel',
        ),
        migrations.DeleteModel(
            name='Label',
        ),
    ]
