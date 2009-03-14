from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime, date
from django.db.models import Count
from calendar import Calendar
from django.contrib.auth.models import User

ACTIVE      = _('Active')
CLOSED      = _('Closed')

CHOICES_STATUS = (('Active',ACTIVE),('Closed',CLOSED))

#class Developer(models.Model):
    
    #nombre          = models.CharField(_('* Nombre'),max_length=100)
    #apellido        = models.CharField(_('* Apellido'),max_length=100)
    #email           = models.EmailField(_('* Email'))
    #nombreusuario   = models.CharField(_('* Nombre de usuario'), unique=True, max_length=100, help_text="Cuenta de acceso")
    #password        = models.CharField(_('* Contrasena'), max_length=100)
    
    #def _get_full_name(self):
        #'''Returns the developer's full name'''
        #return _(u'%s %s')%(self.nombre, self.apellido)
    
    #full_name = property(_get_full_name)
    
    #def __unicode__(self):
        #return _(u'%s %s')%(self.nombre, self.apellido)
    
    #class Meta:
        #verbose_name        = _('Developer')
        #verbose_name_plural = _('Developers')
        #ordering 	    = ['nombre','apellido']

class Repositorio(models.Model):
    
    titulo = models.CharField(_('* Titulo'), max_length=100)
    description = models.CharField(_('* Descripcion'), max_length=100)
    users = models.ManyToManyField(User, through='Miembro')
    
    def __unicode__(self):
        return self.titulo
    
    class Meta:
        verbose_name        = _('Repositorio')
        verbose_name_plural = _('Repositorios')
    

class Miembro(models.Model):
    
    user     = models.ForeignKey(User, verbose_name = '* Developer')
    repositorio   = models.ForeignKey(Repositorio, related_name = 'repositorio_lista', verbose_name = '* Repository')
    fecha_ingreso = models.DateField(default=date.today())
    activo        = models.BooleanField(default=True)
    
    def __unicode__(self):
        return _(u'Miembro %s repositorio %s')%(self.user.username, self.repositorio.titulo)
    
    class Meta:
        verbose_name        = _('Miembro')
        verbose_name_plural = _('Miembros')
        ordering            = ['fecha_ingreso']
        
class Mensaje(models.Model):
    
    users      = models.ManyToManyField(User, verbose_name='* Developer')
    asunto         = models.CharField(_('* Asunto'), max_length=100)
    contenido      = models.CharField(_('* Contenido'), max_length=100)
    fecha_creacion = models.DateTimeField(default=datetime.now()) 
    
    def __unicode__(self):
        return _(u'asunto: %s')%(self.asunto)
    
class Accion(models.Model):
    
    user   = models.ForeignKey(User)
    repositorio = models.ForeignKey(Repositorio)
    commit      = models.CharField(max_length=250)
    fecha_efectuada = models.DateField()
    
    def __unicode__(self):
        return _(u'Commit: %s')%(self.commit)
    
    class Meta:
        verbose_name        = _('Accion')
        verbose_name_plural = _('Acciones')
        ordering            = ['fecha_efectuada']
