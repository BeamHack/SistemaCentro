from django.db import models

class Seguro(models.Model):
	nombre=models.CharField(max_length=140)
	descripcion=models.TextField(blank=True)
	email=models.EmailField()

	def __unicode__(self):
		return self.nombre
