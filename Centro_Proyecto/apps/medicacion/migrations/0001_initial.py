# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
                ('cantidad', models.PositiveIntegerField()),
                ('informacionExtra', models.CharField(max_length=140)),
                ('seguro', models.ForeignKey(to='paciente.Paciente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
