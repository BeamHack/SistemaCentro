# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicacion', '0011_remove_medicamento_receta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='unidad',
            field=models.CharField(default=b'Tab', max_length=20, choices=[(b'Tab', b'Tab'), (b'Unidad', b'Unidad'), (b'Ml', b'Ml'), (b'Mg', b'Mg')]),
            preserve_default=True,
        ),
    ]
