# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0003_post_edited_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=42)),
                ('email', models.EmailField(max_length=75)),
                ('website', models.URLField(null=True, blank=True)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='edited_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.OneToOneField(to='site1.Post'),
        ),
    ]
