# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='activo',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='id',
        ),
        migrations.AddField(
            model_name='paciente',
            name='Numero_Historia',
            field=models.PositiveIntegerField(default=2015, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
