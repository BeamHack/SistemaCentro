from django.db import models
from apps.paciente.models import Paciente
''''
class Receta(models.Model):
	descripcion=models.CharField(max_length=50)
	fecha=models.DateField(auto_now=True)
	libro=models.CharField(max_length=50)
	paciente=models.ForeignKey(Paciente)
	
	def __unicode__(self):
		return self.descripcion
		'''