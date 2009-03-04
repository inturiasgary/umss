from django.db import models

class GrupoTarea(models.Model):
    titulo = models.CharField(max_length=100)

class Tarea(models.Model):
    grupotarea = models.ForeignKey(GrupoTarea)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=(('re','Realizado'),('pe','Pendiente')))
