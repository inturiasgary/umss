from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime, date
from django.db.models import Count
from calendar import Calendar
#from sistema.repository.models import Repository

ACTIVE     = _('Active')
CLOSED      = _('Closed')

CHOICES_STATUS = (('Active',ACTIVE),('Closed',CLOSED))


class Developer(models.Model):
    
    first_name = models.CharField(_('* First name'),max_length=100)
    last_name  = models.CharField(_('* Last name'),max_length=100, null=True, blank=True)
    email      = models.EmailField(_('* Email'), help_text="User login.")
    password   = models.CharField(_('* Password'), max_length=100)
    
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
    
    name = models.CharField(_('* Name'), max_length=100)
    description = models.CharField(_('* Description'), max_length=100)
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
    

class ToDo(models.Model):
    
    repository   = models.ForeignKey(Repository, related_name='todo_repository_list', verbose_name='* Repository')
    title        = models.CharField(_('*Title'),max_length=100)
    state        = models.CharField(choices=CHOICES_STATUS, max_length = 100, default=ACTIVE.decode())
    date_created = models.DateTimeField(default=datetime.now()) 
    
    def __unicode__(self):
        return _(u'%s of %s')%(self.title, self.repository.name)
    
    class Meta:
        verbose_name        = _('ToDo')
        verbose_name_plural = _('ToDo')
        ordering            = ['date_created']

class Task(models.Model):
    
    #developer    = models.CharField()
    todo         = models.ForeignKey(ToDo, related_name='todo_list', verbose_name='* TodoList')
    title        = models.CharField(_('* Title'), max_length=100)
    task         = models.CharField(_('* Task'), max_length=100)
    date_created = models.DateTimeField(default=datetime.now())
    state        = models.CharField(choices=CHOICES_STATUS, max_length = 100, default=ACTIVE.decode())
    
    def __unicode__(self):
        return _(u'%s in %s')%(self.title, self.todo.title)
    
    class Meta:
        verbose_name        = _('Task')
        verbose_name_plural = _('Taks')
        ordering            = ['date_created']

class Action(models.Model):
    
    detail     = models.CharField(_('detail'), max_length=100)
    repository = models.ForeignKey(Repository, related_name='action_repository_list', verbose_name='* Repository')
    time       = models.DateTimeField()
    
    def __unicode__(self):
        return _(u'%s in %s')%(self.detail, self.repository.name)
    
    class Meta:
        verbose_name        = _('Action')
        verbose_name_plural = _('Actions')
        ordering            = ['-time']
        

# Create your models here.
