# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicacion', '0003_medicamento_unidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='unidad',
            field=models.CharField(default=b'TAB', max_length=20, choices=[(b'TAB', b'TAB'), (b'UNIDAD', b'UNIDAD'), (b'ML', b'ML')]),
            preserve_default=True,
        ),
    ]
