# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='purchase_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 26, 16, 2, 52, 848000, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computer',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2023, 12, 26, 16, 3, 26, 533000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
