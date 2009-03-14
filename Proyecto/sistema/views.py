from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader  import get_template
from django.contrib.auth.models import User
from django.contrib.auth import logout
from models import Miembro, Repositorio
from django.utils.translation import ugettext as _
from forms import RegistracionForm

def principal(request):
    return render_to_response("home.html", RequestContext(request))

def latest_developer(request):
    developer_list = Miembro.objects.all()
    return render_to_response('latest_developer.html', {'developer_list':developer_list})

def dev_page(request, nombreusuario):
    try:
        user = User.objects.get(username=nombreusuario)
    except:
        raise Http404(_(u'Nombre de usuario no encontrado'))
    repositorios = Repositorio.objects.filter(users__username=nombreusuario)
    template = get_template('pagina_usuario.html')
    variables = RequestContext (request, {
        'nombreusuario':nombreusuario,
        'repositorios':repositorios
    })
    output = template.render(variables)
    return render_to_response('pagina_usuario.html', variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def register_page(request):
    if request.method == 'POST':
        form = RegistracionForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'],
                                            username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            email=form.cleaned_data['email'])
            return HttpResponseRedirect('/')
    else:
        form = RegistracionForm()
    variables = RequestContext(request, {'form':form})
    return render_to_response('registration/register_user.html', variables)