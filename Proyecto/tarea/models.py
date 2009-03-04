from django.db import models
from sistema.models import Developer, Repository

class TodoList(models.Model):
    title = models.CharField(max_length=100)
    repository = models.ForeignKey(Repository, related_name='todolist', verbose_name='Repositories')

class Todo(models.Model):
    todolist = models.ForeignKey(TodoList, related_name='todos', verbose_name='TodoList')
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=(('re','Realizado'),('pe','Pendiente')))
