from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime, date
from django.db.models import Count
from calendar import Calendar
from django.contrib.auth.models import User
#from sistema.repository.models import Repository

ACTIVE     = _('Active')
CLOSED      = _('Closed')

CHOICES_STATUS = (('Active',ACTIVE),('Closed',CLOSED))


class Developer(User):
    
    first_name      = models.CharField(_('* Nombre'),max_length=100)
    last_name       = models.CharField(_('* Apellido'),max_length=100)
    email           = models.EmailField(_('* Email'), help_text="Cuenta de acceso.")
    password        = models.CharField(_('* Contrasena'), max_length=100)
    activation_date = models.DateField(default=date.today())
    
    def _get_full_name(self):
        '''Returns the developer's full name'''
        return _(u'%s %s')%(self.first_name, self.last_name)
    
    full_name = property(_get_full_name)
    
    def __unicode__(self):
        return _(u'%s %s')%(self.first_name, self.last_name)
    
    class Meta:
        verbose_name        = _('Developer')
        verbose_name_plural = _('Developers')
        ordering 	    = ['first_name','last_name']

class Repository(models.Model):
    
    name = models.CharField(_('* Nombre'), max_length=100)
    description = models.CharField(_('* Descripcion'), max_length=100)
    developers = models.ManyToManyField(Developer, through='Membership')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name        = _('Repository')
        verbose_name_plural = _('Repositories')
    

class Membership(models.Model):
    
    developer   = models.ForeignKey(Developer, related_name = 'developerlist', verbose_name = '* Developer')
    repository  = models.ForeignKey(Repository, related_name = 'repository_list', verbose_name = '* Repository')
    date_joined = models.DateField(default=date.today())
    active      = models.BooleanField(default=True)
    
    def __unicode__(self):
        return _(u'Membership of Dev. %s %s and repository %s')%(self.developer.first_name, self.developer.last_name, self.repository.name)
    
    class Meta:
        verbose_name        = _('Membership')
        verbose_name_plural = _('Memberships')
        ordering            = ['date_joined']
        
class Message(models.Model):
    
    developer    = models.ForeignKey(Developer, related_name = 'developer_list', verbose_name='* Developer')
    subject      = models.CharField(_('*Subject'), max_length=100)
    content      = models.CharField(_('*Content'), max_length=100)
    date_created = models.DateTimeField(default=datetime.now()) 
    
    def __unicode__(self):
        return _(u'subject')%(self.subject)
