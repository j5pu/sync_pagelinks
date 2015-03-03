# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phasionate', '0003_wp9posts'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='wpposts',
            table='wp_9_posts',
        ),
    ]
