# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PagelinkPost',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('pagelink_id', models.CharField(db_index=True, max_length=50, null=True, blank=True)),
                ('post_id', models.CharField(db_index=True, max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('post_id', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('link', models.URLField(null=True, blank=True)),
                ('title', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('description', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('image', models.URLField(null=True, blank=True)),
                ('hashtag', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
