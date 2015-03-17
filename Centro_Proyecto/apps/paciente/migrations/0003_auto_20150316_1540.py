# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0002_auto_20150316_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='Numero_Historia',
            field=models.PositiveIntegerField(unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
