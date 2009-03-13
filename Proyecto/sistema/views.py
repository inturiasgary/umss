from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse, Http404
from django.template.loader  import get_template
from models import Miembro, Developer, Repositorio
from django.utils.translation import ugettext as _

def principal(request):
    template = get_template('base.html')
    variables = Context ({
        'head_title':'Herramienta colaborativa',
        'page_title':'Bienvenido a la herramienta',
        'page_body' :'Donde tu puedes compartir el desarrollo',
    })
    output = template.render(variables)
    return HttpResponse(output)

def latest_developer(request):
    developer_list = Miembro.objects.all()
    return render_to_response('latest_developer.html', {'developer_list':developer_list})

def dev_page(request, nombreusuario):
    try:
        user = Developer.objects.get(nombreusuario=nombreusuario)
    except:
        raise Http404(_(u'Nombre de usuario no encontrado'))
    repositorios = Repositorio.objects.filter(developers__nombreusuario=nombreusuario)
    template = get_template('pagina_usuario.html')
    variables = Context ({
        'nombreusuario':nombreusuario,
        'repositorios':repositorios
    })
    output = template.render(variables)
    return HttpResponse(output)
    