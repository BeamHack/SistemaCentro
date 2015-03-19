# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
        ('receta', '0002_delete_receta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now=True)),
                ('libro', models.CharField(max_length=50)),
                ('paciente', models.ForeignKey(to='paciente.Paciente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
