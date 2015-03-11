# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicacion', '0002_auto_20150308_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='unidad',
            field=models.CharField(default=b'TAB', max_length=20, choices=[(b'TAB', b'TAB'), (b'MG', b'MG')]),
            preserve_default=True,
        ),
    ]
