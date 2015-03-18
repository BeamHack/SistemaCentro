from django.db import models
from apps.seguro.models import Seguro

class Paciente(models.Model):
	Numero_Historia=models.PositiveIntegerField(max_length=4, primary_key=True, unique=True, null=False)
	activo=models.BooleanField(default=True)
	Mujer="Mujer"
	Hombre="Hombre"
	cedula=models.IntegerField( unique=True)
	nombre=models.CharField(max_length=140)
	apellido=models.CharField(max_length=140)
	Sexos=((Mujer, "Mujer"), (Hombre, "Hombre"))
	sexo=models.CharField(max_length=20, choices=Sexos,default=Hombre)
	foto=models.ImageField(upload_to="fotos")
	ciudad=models.CharField(max_length=140)
	correo=models.EmailField()
	direccion=models.CharField( max_length=140)
	representanteLegal=models.CharField(max_length=140)
	fechaIngreso=models.DateField(auto_now=True)
	edad=models.PositiveIntegerField()
	Fecha_nacimiento=models.DateField()
	nacionalidad=models.CharField(max_length=140)
	grado_de_Instruccion=models.CharField(max_length=140)
	descripcion_clinica=models.TextField()
	seguro=models.ForeignKey(Seguro)
		
	def __unicode__(self):
		return "%s -%s"% (self.nombre, self.apellido)