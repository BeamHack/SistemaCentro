# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicacion', '0005_auto_20150308_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='nombre',
            field=models.CharField(unique=True, max_length=140),
            preserve_default=True,
        ),
    ]
