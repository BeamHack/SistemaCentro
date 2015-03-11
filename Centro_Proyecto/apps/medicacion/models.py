from django.db import models
from apps.paciente.models import Paciente

class Medicamento(models.Model):
	nombre=models.CharField(max_length=140)
	cantidad=models.PositiveIntegerField()
	informacion_Extra=models.CharField(max_length=140)
	TAB="TAB"
	MG="MG"
	UNIDAD="UNIDAD"
	ML="ML"
	Unidades=((TAB, "TAB"), (UNIDAD, "UNIDAD"),(ML, "ML"),(MG, "MG"))
	unidad=models.CharField(max_length=20, choices=Unidades,default=TAB)
	paciente=models.ForeignKey(Paciente)
		
	def __unicode__(self):
		return  self.nombre
