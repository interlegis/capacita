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
        orgao_id = request.user.profile.orgao_id
        orgao = Orgao.objects.get(cod_orgao = orgao_id).nome
        profiles = Profile.objects.filter(orgao_id = orgao_id)
        users = []

        for profile in profiles:
            if (User.objects.get(id = profile.user_id) != request.user):
                users.append(User.objects.get(id = profile.user_id))
        admin = is_admin(request)
        group = Group.objects.get(name='gestor')
        group2 = Group.objects.get(name='admin')

    else:
        profiles = Profile.objects.all().exclude(ind_excluido = True)
        orgao = ""
        group2 = group = None

        if ((group2 in request.user.groups.all())):
            users = User.objects.exclude(id = request.user.id)

    if (group2 in request.user.groups.all()):
        users = User.objects.exclude(id = request.user.id)
        orgaos = Orgao.objects.all()
        orgao = ''

        if request.GET.get('orgao', ''):

            user_orgao = request.GET.get('orgao', '')

            profiles = Profile.objects.filter(orgao_id = user_orgao)
            users = []

            for profile in profiles:
                if (User.objects.get(id = profile.user_id) != request.user):
                    users.append(User.objects.get(id = profile.user_id))

        return render(request, 'usuarios.html', {'users' : users, 'profiles' : profiles, 'orgao' : orgao, 'orgaos' : orgaos})
    else:
        if ((group in request.user.groups.all())):
            return render(request, 'usuarios.html', {'users' : users, 'profiles' : profiles, 'orgao' : orgao})
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
def usuario_edit(request, pk):
    usuario = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        form = UserForm(request.POST, instance=usuario)
        id_group = request.POST['group']
        my_group = Group.objects.get(id=id_group)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.groups.clear()
            profile = Profile.objects.get(user_id = usuario.id)
            profile.orgao_id = request.POST['orgao']
            profile.save()
            my_group = Group.objects.get(id=id_group)
            usuario.groups.add(my_group)
            usuario.is_active = True
            usuario.save()

            return redirect("usuarios")
    else:
        form = UserForm(instance=usuario)
        orgaos = Orgao.objects.all()
        groups = Group.objects.all()

    groups = Group.objects.all()
    orgaos = Orgao.objects.all()

    if is_admin(request):
        return render(request, 'usuario_edit.html', {'form': form, 'orgaos' : orgaos, 'groups' : groups, 'usuario' : usuario})
    else:
        return redirect('error')
