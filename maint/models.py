#encoding:utf-8

from django.db import models
# Create your models here.

class Ponente(models.Model):
	titulo = models.CharField(max_length=200, blank = True, null = True)
	nombre = models.CharField(max_length = 200)
	apellidos = models.CharField(max_length = 250)
	cargo = models.CharField(max_length = 250)
	institucion = models.CharField(max_length = 250)
	pais = models.CharField(max_length = 250)
	curriculum = models.TextField(blank = True, null = True)
	foto = models.FileField(upload_to="ponentes")

	def __unicode__(self):
		return "%s %s  (%s)" %(self.nombre, self.apellidos, self.pais)


class Evento(models.Model):
	nombre = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.nombre


class Sala(models.Model):
	nombre = models.CharField(max_length = 200)
	direccion = models.CharField(max_length = 250)

	def __unicode__(self):
		return self.nombre


class Ponencia(models.Model):
	ponente = models.ForeignKey(Ponente)
	titulo = models.CharField(max_length = 255)
	resumen = models.TextField(blank = True, null = True)
	fecha  = models.DateTimeField()
	evento = models.ForeignKey(Evento)
	sala = models.ForeignKey(Sala)

	def __unicode__(self):
		return u"%s: %s" %(self.ponente, self.titulo)

TIPOSTAND = (
    ('institucion',u'Institución'),
    ('empresa','Empresa'),    
)

class Stand(models.Model):
	nombre = models.CharField(max_length = 250)
	dedicacion = models.TextField(blank = True, null = True)
	tipo = models.CharField(max_length=50, choices=TIPOSTAND)
	web = models.URLField(blank = True, null = True)
	email = models.EmailField(blank = True, null = True)
	telefono = models.CharField(max_length = 50, blank = True, null = True)
	pais = models.CharField(max_length = 150)
	provincia = models.CharField(max_length = 150, blank = True, null = True)
	localidad = models.CharField(max_length = 150, blank = True, null = True)
	direccion = models.CharField(max_length = 150, blank = True, null = True)

	def __unicode__(self):
		return u'%s' %(self.nombre)