# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_module', '0006_citymodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorbiomodel',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Picture'),
        ),
    ]
