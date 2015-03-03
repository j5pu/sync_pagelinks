# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150303_1139'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
