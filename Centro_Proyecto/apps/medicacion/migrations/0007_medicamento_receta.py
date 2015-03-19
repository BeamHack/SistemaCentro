# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0001_initial'),
        ('medicacion', '0006_auto_20150315_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='receta',
            field=models.ForeignKey(default=2015, to='receta.Receta'),
            preserve_default=False,
        ),
    ]
