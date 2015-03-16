# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicacion', '0010_auto_20150315_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicamento',
            name='receta',
        ),
    ]
