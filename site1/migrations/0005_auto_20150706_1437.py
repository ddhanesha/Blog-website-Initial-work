# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0004_auto_20150706_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='website',
        ),
    ]
