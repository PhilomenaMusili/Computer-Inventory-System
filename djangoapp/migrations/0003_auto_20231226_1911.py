# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_auto_20231226_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='purchase_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
