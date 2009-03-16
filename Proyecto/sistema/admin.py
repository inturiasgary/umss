from django.contrib import admin
from models import Repository, MemberShip, Mensaje, Accion, Tag

admin.site.register(Repository)
admin.site.register(MemberShip)
admin.site.register(Mensaje)
admin.site.register(Accion)
admin.site.register(Tag)