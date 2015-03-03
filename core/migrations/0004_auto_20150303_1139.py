# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150302_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagelinkpost',
            name='pagelink_id',
            field=models.CharField(default=None, max_length=50, null=True, db_index=True, blank=True),
            preserve_default=True,
        ),
    ]
