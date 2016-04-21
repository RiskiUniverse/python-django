# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZingChartConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('xAxis', models.CharField(max_length=20)),
                ('yAxis', models.CharField(max_length=20)),
                ('theme', models.CharField(max_length=20)),
                ('dangerRangeLow', models.IntegerField()),
                ('dangerRangeHigh', models.IntegerField()),
            ],
            options={
                'db_table': 'zingchart_config',
            },
        ),
        migrations.CreateModel(
            name='ZingChartSeriesData1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('temperature', models.IntegerField()),
            ],
            options={
                'db_table': 'zingchart_data_1',
            },
        ),
        migrations.CreateModel(
            name='ZingChartSeriesData2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('temperature', models.IntegerField()),
            ],
            options={
                'db_table': 'zingchart_data_2',
            },
        ),
        migrations.CreateModel(
            name='ZingChartSeriesData3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('temperature', models.IntegerField()),
            ],
            options={
                'db_table': 'zingchart_data_3',
            },
        ),
    ]
