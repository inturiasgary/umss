from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader  import get_template
from django.contrib.auth.models import User
from django.contrib.auth import logout
from models import MemberShip, Repository, Tag
from django.utils.translation import ugettext as _
from forms import RegistracionForm, RepositorySaveForm
from django.contrib.auth.decorators import login_required

def principal(request):
    return render_to_response("home.html", RequestContext(request))

def latest_developer(request):
    developer_list = MemberShip.objects.all()
    return render_to_response('latest_developer.html', {'developer_list':developer_list})

@login_required
def dev_page(request, nombreusuario):
    try:
        user = User.objects.get(username=nombreusuario)
    except:
        raise Http404(_(u'Nombre de usuario no encontrado'))
    repositorios = Repository.objects.filter(users__username=nombreusuario)
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
            user = User.objects.create(first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'],
                                            username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            )
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return HttpResponseRedirect('/sistema/registro/realizado/')
    else:
        form = RegistracionForm()
    variables = RequestContext(request, {'form':form})
    return render_to_response('registration/register_user.html', variables)

@login_required
def repository_save_page(request):
    if request.method == 'POST':
        form = RepositorySaveForm(request.POST)
        if form.is_valid():
            #user = User.objects.get(username=request.user.username)
            repository, created = Repository.objects.get_or_create( title=form.cleaned_data['title'],
                                                                    description=form.cleaned_data['description'])
            #Si el repositorio esta siendo actualizado
            if not created:
                repository.tag_set.clear()
            tag_names = form.cleaned_data['tags'].split()
            for tag_name in tag_names:
                tag, dummy = Tag.objects.get_or_create(name=tag_name)
                repository.tag_set.add(tag)
            #guardado del repositorio
            repository.save()
            #haciendo miembro del repositorio al creador
            m1 = MemberShip(user=request.user, repository=repository)
            m1.save()
            return HttpResponseRedirect(
            '/sistema/dev/%s' % request.user.username)
    else:
        form = RepositorySaveForm()
    variables = RequestContext(request, 
                               {'form':form})
    return render_to_response('repository_save.html', variables)
            