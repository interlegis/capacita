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
    if (hasattr(request.user, 'profile')):
        users = User.objects.all()
        profiles = Profile.objects.all()
        orgaos = Orgao.objects.all()
        return render(request, 'usuarios.html', {'users' : users, 'profiles' : profiles, 'orgaos' : orgaos})
    else:
        return render(request, 'error.html')

@login_required
def usuario_new(request):
    admin = is_admin(request)
    if request.method == 'POST' and admin:
        form = UserForm(request.POST)
        id_group = request.POST['group']
        my_group = Group.objects.get(id=id_group)
        if form.is_valid():
            user_check = User.objects.filter(username='zequinha').count()
            if(user_check == 0):
                usuario = form.save()
                profile = Profile.objects.create(orgao_id = request.POST['orgao'], user_id = usuario.id)
                usuario.is_active = True
                usuario.groups.add(my_group)
                profile.save()
                usuario.save()
            else:
                return render(request, 'usuario_edit.html', {'form' : form, 'orgaos' : orgaos, 'groups' : groups, 'usuario' : True})

            return redirect("usuarios")
        else:
            return render(request, 'usuario_edit.html', {'form' : form})
    elif request.method != 'POST':
        form = UserForm()
        orgaos = Orgao.objects.all()
        groups = Group.objects.all()
    else:
        return render(request, 'error.html')

    orgaos = Orgao.objects.all()
    groups = Group.objects.all()

    if admin:
        return render(request, 'usuario_edit.html', {'form' : form, 'orgaos' : orgaos, 'groups' : groups, 'usuario' : True})
    else:
        return redirect('error')

@login_required
def usuario_orgao_adicionar(request, pk):
    profile = Profile.objects.get(pk = pk)

    print("PERMISSAO = ", profile)
    if request.method == "POST":
        if profile.orgao_ativo == request.POST['orgao']:
            profile.orgao_ativo = null
        permissao = OrgaoPermissao.objects.get(orgao_id = request.POST['orgao'], grupo_id = 2)
        profile.orgaos.add(permissao)

    groups = Group.objects.all()
    orgaos_usuario = profile.orgaos.filter(grupo_id = 2)
    orgaos = Orgao.objects.all().exclude(cod_orgao__in = [orgao.orgao_id for orgao in orgaos_usuario])
    if is_admin(request):
        return render(request, 'usuario_orgao.html', {'profile_user': profile, 'orgaos' : orgaos, 'groups' : groups, 'orgaos_usuario' : orgaos_usuario})
    else:
        return redirect('error')

@login_required
def usuario_orgao_deletar(request, pk, orgao):
    profile = Profile.objects.get(pk = pk)
    if profile.orgao_ativo == orgao:
        profile.orgao_ativo = null
    permissao = OrgaoPermissao.objects.get(orgao_id = orgao, grupo_id = 2)
    profile.orgaos.remove(permissao)
    if is_admin(request):
        return redirect("usuario_orgao_adicionar", pk=pk)
    else:
        return redirect('error')


@login_required
def usuario_edit(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    profile = Profile.objects.get(user_id = usuario.id)

    if request.method == "POST":
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.groups.clear()
            profile.orgao_id = request.POST['orgao']
            profile.save()
            usuario.is_active = True
            usuario.save()

            return redirect("usuarios")
    else:
        form = UserForm(instance=usuario)
        orgaos = Orgao.objects.all()
        groups = Group.objects.all()

    groups = Group.objects.all()
    orgaos = Orgao.objects.all()
    orgaos_usuario = profile.orgaos.filter(grupo_id = 2)

    if is_admin(request):
        return render(request, 'usuario_edit.html', {'form': form, 'orgaos' : orgaos, 'groups' : groups, 'usuario' : usuario, 'orgaos_usuario' : orgaos_usuario})
    else:
        return redirect('error')
