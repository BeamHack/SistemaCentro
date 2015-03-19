# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicacion', '0009_medicamento_receta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='receta',
            field=models.OneToOneField(to='receta.Receta'),
            preserve_default=True,
        ),
    ]
