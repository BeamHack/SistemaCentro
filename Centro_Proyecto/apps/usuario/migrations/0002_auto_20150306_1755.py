# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='apellido',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nombre',
            new_name='last_name',
        ),
    ]
