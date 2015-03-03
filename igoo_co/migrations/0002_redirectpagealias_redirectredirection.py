# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('igoo_co', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedirectPagealias',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('uri', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'redirect_pagealias',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RedirectRedirection',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=200, blank=True)),
                ('platform', models.IntegerField(null=True, blank=True)),
                ('language', models.CharField(max_length=2, blank=True)),
            ],
            options={
                'db_table': 'redirect_redirection',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
