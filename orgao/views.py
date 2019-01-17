from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from usuario.urls import *
from usuario.views import *
from capacitaApp.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from capacita.template_context_processors import is_admin

@login_required
def orgao(request):
    if (hasattr(request.user, 'profile')):
        orgaos_list = Orgao.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(orgaos_list, 10)
        permissao = False
        paginator = Paginator(orgaos_list, 6)
        if is_admin(request)['is_admin']:
            try:
                orgaos = paginator.page(page)
            except PageNotAnInteger:
                orgaos = paginator.page(1)
            except EmptyPage:
                orgaos = paginator.page(paginator.num_pages)
            return render(request, 'orgao.html', {'orgaos' : orgaos})
        else:
            return render(request, 'error.html')
    else:
        return redirect('error')

@login_required
def orgao_edit(request, pk):
    admin = is_admin(request)['is_admin']
    orgao = get_object_or_404(Orgao, pk=pk)
    if request.method == "POST" and admin:
        form = OrgaoForm(request.POST, instance=orgao)
        if form.is_valid():
            orgao = form.save()
            return redirect('orgao')
        else:
            return render(request, 'orgao_edit.html', {'form': form})
    elif request.method != "POST" and admin:
        form = OrgaoForm(instance=orgao)
        return render(request, 'orgao_edit.html', {'form': form})
    else:
        return render(request, 'error.html')

@login_required
def orgao_new(request):
    admin = is_admin(request)['is_admin']
    if request.method == "POST" and admin:
        form = OrgaoForm(request.POST)
        if form.is_valid():
            orgao = form.save()
            return redirect('orgao')
        else:
            return render(request, 'orgao_edit.html', {'form': form})
    elif request.method != "POST" and admin:
        form = OrgaoForm()
        return render(request, 'orgao_edit.html', {'form': form})
    else:
        return render(request, 'error.html')

@login_required
def orgao_delete(request, id):
    admin = is_admin(request)['is_admin']
    if admin:
        Orgao.objects.filter(pk=id).update(ind_excluido=1)
        return redirect("orgao")
    else:
        return render(request, 'error.html')

@login_required
def orgao_undelete(request, id):
    admin = is_admin(request)['is_admin']
    if admin:
        Orgao.objects.filter(pk=id).update(ind_excluido=0)
        return redirect("orgao")
    else:
        return render(request, 'error.html')

@login_required
def gestores_orgao(request, pk):
    if (hasattr(request.user, 'profile')) and is_admin(request)['is_admin']:
        orgao_escolhido = Orgao.objects.get(pk=pk)
        permissao = OrgaoPermissao.objects.get(orgao_id = pk, grupo_id = 2)
        if request.method == "POST":
            profile = Profile.objects.get(pk = request.POST['usuario'])
            profile.orgaos.add(permissao)

        profiles_orgao = Profile.objects.filter(orgaos = permissao)
        profiles = Profile.objects.exclude(orgaos = permissao)
        users = User.objects.all()
        return render(request, 'gestores_orgao.html', {'users' : users, 'profiles' : profiles, 'profiles_orgao' : profiles_orgao, 'orgao_escolhido': orgao_escolhido})
    else:
        return render(request, 'error.html')
