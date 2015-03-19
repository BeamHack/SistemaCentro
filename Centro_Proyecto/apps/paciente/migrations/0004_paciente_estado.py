# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_auto_20150316_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='estado',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
