# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='creator',
            field=models.CharField(max_length=32, blank=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
