# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phasionate', '0004_auto_20150302_1742'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='wpposts',
            table='wp_posts',
        ),
    ]
