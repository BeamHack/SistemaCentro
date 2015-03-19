# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicacion', '0012_auto_20150316_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='nombre',
            field=models.CharField(max_length=140),
            preserve_default=True,
        ),
    ]
