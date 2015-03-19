from django.db import models
from apps.paciente.models import Paciente
#from apps.receta.models import Receta

class Medicamento(models.Model):
	nombre=models.CharField(max_length=140)
	cantidad=models.PositiveIntegerField()
	informacion_Extra=models.CharField(max_length=140)
	Tab="Tab"
	Mg="Mg"
	Unidad="Unidad"
	Ml="Ml"
	Unidades=((Tab, "Tab"), (Unidad, "Unidad"),(Ml, "Ml"),(Mg, "Mg"))
	unidad=models.CharField(max_length=20, choices=Unidades,default=Tab)
	#receta=models.OneToOneField(Receta)
	paciente=models.ForeignKey(Paciente)
		
	def __unicode__(self):
		return  self.nombre
