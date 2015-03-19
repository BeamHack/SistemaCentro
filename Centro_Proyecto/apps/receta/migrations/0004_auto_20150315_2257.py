# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicacion', '0011_remove_medicamento_receta'),
        ('receta', '0003_receta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='paciente',
        ),
        migrations.DeleteModel(
            name='Receta',
        ),
    ]
