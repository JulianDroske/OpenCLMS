# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-14 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_system', '0003_auto_20170807_1729'),
        ('checkin', '0004_checkinhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailySubscibe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_system.User')),
            ],
        ),
    ]
