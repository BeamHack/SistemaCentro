# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0004_paciente_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='estado',
            new_name='activo',
        ),
    ]
