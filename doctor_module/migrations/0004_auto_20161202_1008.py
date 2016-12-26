# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_module', '0003_auto_20161202_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degreemodel',
            name='instititute_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='degreemodel',
            name='institute_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='designationmodel',
            name='instititute_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='designationmodel',
            name='institute_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hospitalinfmodel',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='specialistmodel',
            name='instititute_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='specialistmodel',
            name='institute_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]