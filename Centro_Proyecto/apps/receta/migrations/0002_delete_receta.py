# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicacion', '0008_remove_medicamento_receta'),
        ('receta', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Receta',
        ),
    ]
