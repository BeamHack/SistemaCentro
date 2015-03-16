# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicacion', '0007_medicamento_receta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicamento',
            name='receta',
        ),
    ]
