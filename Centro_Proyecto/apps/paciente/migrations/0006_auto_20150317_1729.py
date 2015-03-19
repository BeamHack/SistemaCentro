# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0005_auto_20150316_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='Numero_Historia',
            field=models.PositiveIntegerField(max_length=4, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
