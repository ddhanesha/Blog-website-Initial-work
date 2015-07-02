# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0002_auto_20150630_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
