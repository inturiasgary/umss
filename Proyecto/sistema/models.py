from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime, date
from django.db.models import Count
from calendar import Calendar
from django.contrib.auth.models import User

ACTIVE      = _('Active')
CLOSED      = _('Closed')

CHOICES_STATUS = (('Active',ACTIVE),('Closed',CLOSED))

class Repository(models.Model):
    
    title       = models.CharField(_('* Titulo'), max_length=100, unique=True)
    description = models.CharField(_('* Descripcion'), max_length=100)
    users       = models.ManyToManyField(User, through='MemberShip')
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name        = _('Repositorio')
        verbose_name_plural = _('Repositorios')
        
class Tag(models.Model):
    
    name        = models.CharField(max_length=64, unique=True)
    repository  = models.ManyToManyField(Repository)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name        = _('Tag')
        verbose_name_plural = _('Tags')
    

class MemberShip(models.Model):
    
    user        = models.ForeignKey(User, verbose_name = '* Developer')
    repository  = models.ForeignKey(Repository, related_name = 'repositorio_lista', verbose_name = '* Repository')
    date_in     = models.DateField(default=date.today())
    state       = models.BooleanField(default=True)
    
    def __unicode__(self):
        return _(u'Miembro %s repositorio %s')%(self.user.username, self.repository.title)
    
    class Meta:
        verbose_name        = _('Miembro')
        verbose_name_plural = _('Miembros')
        ordering            = ['date_in']
        
class Mensaje(models.Model):
    
    users        = models.ManyToManyField(User, verbose_name='* Developer')
    subject      = models.CharField(_('* Asunto'), max_length=100)
    content      = models.CharField(_('* Contenido'), max_length=100)
    created_date = models.DateTimeField(default=datetime.now()) 
    
    def __unicode__(self):
        return _(u'asunto: %s')%(self.subject)
    
class Accion(models.Model):
    
    user         = models.ForeignKey(User)
    repository   = models.ForeignKey(Repository)
    commit       = models.CharField(max_length=250)
    created_date = models.DateField()
    
    def __unicode__(self):
        return _(u'Commit: %s')%(self.commit)
    
    class Meta:
        verbose_name        = _('Accion')
        verbose_name_plural = _('Acciones')
        ordering            = ['created_date']
