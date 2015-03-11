# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicamento',
            old_name='informacionExtra',
            new_name='informacion_Extra',
        ),
        migrations.RenameField(
            model_name='medicamento',
            old_name='seguro',
            new_name='paciente',
        ),
    ]
