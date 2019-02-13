from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from capacita.template_context_processors import is_admin

@login_required
def usuarios(request):
    if hasattr(request.user, 'profile') and is_admin(request)['is_admin']:
        try:
            orgao_escolhido = int(request.POST['orgao'])
            profiles = Profile.objects.filter(orgaos__pk = orgao_escolhido)
        except Exception as e:
            orgao_escolhido = ''
            profiles = Profile.objects.all()

        users = User.objects.all()
        orgaos = Orgao.objects.all()
        return render(request, 'usuarios.html', {'users' : users, 'profiles' : profiles, 'orgaos' : orgaos, 'orgao_escolhido': orgao_escolhido})
    else:
        return render(request, 'error.html')

@login_required
def usuario_new(request):
    admin = is_admin(request)['is_admin']
    if request.method == 'POST' and admin:
        form = UserForm(request.POST)
        if form.is_valid():
            user_check = User.objects.filter(username=form.fields['username']).count()
            if(user_check == 0):
                usuario = form.save()
                profile = Profile.objects.create(user_id = usuario.id)
                usuario.is_active = True
                profile.save()
                usuario.save()
                return redirect('usuario:usuarios')
            else:
                return render(request, 'usuario_edit.html', {'form' : form, 'orgaos' : orgaos, 'groups' : groups, 'usuario' : True})

        else:
            return render(request, 'usuario_edit.html', {'form' : form})
    elif request.method != 'POST':
        form = UserForm()
        orgaos = Orgao.objects.all()
        groups = Group.objects.all()
    else:
        return render(request, 'error.html')

    orgaos = Orgao.objects.all()

    if admin:
        return render(request, 'usuario_edit.html', {'form' : form, 'orgaos' : orgaos, 'usuario' : True})
    else:
        return redirect('error')

@login_required
def usuario_orgao_adicionar(request, pk):
    profile = Profile.objects.get(pk = pk)
    if request.method == "POST" and is_admin(request)['is_admin']:
        if not profile.orgao_ativo:
            profile.orgao_ativo = Orgao.objects.get(pk=request.POST['orgao'])
            profile.save()
        profile.orgaos.add(request.POST['orgao'])
    elif not is_admin(request)['is_admin']:
        return redirect('error')

    groups = Group.objects.all()
    orgaos_usuario = profile.orgaos.filter()
    orgaos = Orgao.objects.all().exclude(cod_orgao__in = [orgao.pk for orgao in orgaos_usuario])
    return render(request, 'usuario_orgao.html', {'profile_user': profile, 'orgaos' : orgaos, 'groups' : groups, 'orgaos_usuario' : orgaos_usuario})

@login_required
def usuario_orgao_deletar(request, pk, orgao):
    profile = Profile.objects.get(pk = pk)
    profile.orgaos.remove(orgao)
    if profile.orgao_ativo == Orgao.objects.get(pk=orgao) and is_admin(request)['is_admin']:
        if profile.orgaos.count() == 0:
            profile.orgao_ativo = None
            profile.save()
        else:
            profile.orgao_ativo = profile.orgaos.first()
            profile.save()
    elif not is_admin(request)['is_admin']:
        return redirect('error')
    return redirect(request.META['HTTP_REFERER'])


@login_required
def usuario_edit(request, pk):
    profile = get_object_or_404(Profile, id = pk)
    usuario = get_object_or_404(User, pk=profile.user_id)
    if request.method == "POST" and is_admin(request)['is_admin']:
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.is_active = True
            usuario.save()
            return redirect('usuario:usuarios')
    elif request.method != "POST":
        form = UserForm(instance=usuario)
    else:
        return redirect('error')
    groups = Group.objects.all()
    orgaos = Orgao.objects.all()
    orgaos_usuario = profile.orgaos
    return render(request, 'usuario_edit.html', {'form': form, 'orgaos' : orgaos, 'groups' : groups, 'usuario' : usuario, 'orgaos_usuario' : orgaos_usuario})

def admin_approve(request, pk):
    if is_admin(request)['is_admin']:
        Profile.objects.filter(pk=pk).update(is_admin=True)
        return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'error.html')

def admin_disapprove(request, pk):
    if is_admin(request)['is_admin']:
        Profile.objects.filter(pk=pk).update(is_admin=False)
        return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'error.html')
