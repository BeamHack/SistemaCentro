# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguro', '0002_auto_20150307_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.IntegerField(unique=True)),
                ('activo', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=140)),
                ('apellido', models.CharField(max_length=140)),
                ('sexo', models.CharField(default=b'Hombre', max_length=20, choices=[(b'Mujer', b'Mujer'), (b'Hombre', b'Hombre')])),
                ('foto', models.ImageField(upload_to=b'fotos')),
                ('ciudad', models.CharField(max_length=140)),
                ('correo', models.EmailField(max_length=75)),
                ('direccion', models.CharField(max_length=140)),
                ('representanteLegal', models.CharField(max_length=140)),
                ('fechaIngreso', models.DateField(auto_now=True)),
                ('edad', models.PositiveIntegerField()),
                ('Fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=140)),
                ('grado_de_Instruccion', models.CharField(max_length=140)),
                ('descripcion_clinica', models.TextField()),
                ('seguro', models.ForeignKey(to='seguro.Seguro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
