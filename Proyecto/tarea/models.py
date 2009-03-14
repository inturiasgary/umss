from django.db import models
from django.contrib.auth.models import User
from sistema.models import Repositorio
from django.utils.translation import ugettext as _
from datetime import date

class TodoList(models.Model):
    nombre = models.CharField(max_length=100)
    repositorio = models.ForeignKey(Repositorio, related_name='todolist', verbose_name='Repositories')
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name        = _('Todo List')
        verbose_name_plural = _('Todo List')
        
class Todo(models.Model):
    todolist = models.ForeignKey(TodoList, related_name='todos', verbose_name='TodoList')
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=(('re','Realizado'),('pe','Pendiente')))
    fecha_publicacion = models.DateField(default = date.today())
    
    def __unicode__(self):
        return self.titulo
    
    class Meta:
        verbose_name        = _('To do')
        verbose_name_plural = _('To do')
        ordering            = ['fecha_publicacion']

class Comentario(models.Model):
    user              = models.ForeignKey(User)
    todo              = models.ForeignKey(Todo)
    mensaje           = models.CharField(max_length=200)
    fecha_publicacion = models.DateField(default = date.today())
    
    def __unicode__(self):
        return self.mensaje
    
    class Meta:
        verbose_name         = _('Comentario')
        verbose_name_plural  = _('Comentarios')
        ordering             = ['fecha_publicacion']