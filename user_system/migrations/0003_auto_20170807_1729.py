# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_system', '0002_user_mainrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='academiccode',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='accuracy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ip',
            field=models.GenericIPAddressField(null=True, protocol='ipv4'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastlogintime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastpositiontime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='openid',
            field=models.CharField(max_length=28, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wechatdeviceid',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='usertorole',
            name='role',
            field=models.ForeignKey(db_column=b'roleid', on_delete=django.db.models.deletion.CASCADE, to='user_system.Role'),
        ),
        migrations.AlterField(
            model_name='usertorole',
            name='user',
            field=models.ForeignKey(db_column=b'userid', on_delete=django.db.models.deletion.CASCADE, to='user_system.User'),
        ),
    ]
