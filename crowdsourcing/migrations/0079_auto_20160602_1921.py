# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-02 19:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0078_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesteraccesscontrolgroup',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requesteraccesscontrolgroup',
            name='type',
            field=models.SmallIntegerField(choices=[(1, b'allow'), (2, b'deny')], default=1),
        ),
        migrations.AlterField(
            model_name='workeraccesscontrolentry',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
