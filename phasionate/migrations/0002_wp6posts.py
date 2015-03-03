# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phasionate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wp6Posts',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('post_author', models.BigIntegerField()),
                ('post_date', models.DateTimeField()),
                ('post_date_gmt', models.DateTimeField()),
                ('post_content', models.TextField()),
                ('post_title', models.TextField()),
                ('post_excerpt', models.TextField()),
                ('post_status', models.CharField(max_length=20)),
                ('comment_status', models.CharField(max_length=20)),
                ('ping_status', models.CharField(max_length=20)),
                ('post_password', models.CharField(max_length=20)),
                ('post_name', models.CharField(max_length=200)),
                ('to_ping', models.TextField()),
                ('pinged', models.TextField()),
                ('post_modified', models.DateTimeField()),
                ('post_modified_gmt', models.DateTimeField()),
                ('post_content_filtered', models.TextField()),
                ('post_parent', models.BigIntegerField()),
                ('guid', models.CharField(max_length=255)),
                ('menu_order', models.IntegerField()),
                ('post_type', models.CharField(max_length=20)),
                ('post_mime_type', models.CharField(max_length=100)),
                ('comment_count', models.BigIntegerField()),
            ],
            options={
                'db_table': 'wp_6_posts',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
