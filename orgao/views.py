from capacita.decorators import admin_required
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from plano.models import *
from necessidade.models import Necessidade_Orgao
from .models import *
from .forms import *
from usuario.views import *
from capacitaApp.models import *


@login_required
@admin_required
def orgao(request):
    if hasattr(request.user, 'profile'):
        orgaos = Orgao.objects.all()
        return render(request, 'orgao.html', {'orgaos': orgaos})
    else:
        return redirect('error')


@login_required
@admin_required
def orgao_edit(request, pk):
    orgao = get_object_or_404(Orgao, pk=pk)
    if request.method == "POST":
        form = OrgaoForm(request.POST, instance=orgao)
        if form.is_valid():
            form.save()
            return redirect('orgao')
        else:
            return render(request, 'orgao_edit.html', {'form': form})
    else:
        form = OrgaoForm(instance=orgao)
        return render(request, 'orgao_edit.html', {'form': form})

@login_required
@admin_required
def orgao_new(request):
    if request.method == "POST":
        form = OrgaoForm(request.POST)
        if form.is_valid():
            orgao = form.save(commit=False)
            if orgao.cod_superior:
                orgao.nivel = orgao.cod_superior.nivel + 1
            else:
                orgao.nivel = 1
            orgao.save()
            plano = Plano_Capacitacao.objects.filter(plano_habilitado=True)[0]
            Necessidade_Orgao.objects.create(cod_orgao = orgao, cod_plano_capacitacao = plano, estado = False)
            return redirect('orgao')
        else:
            return render(request, 'orgao_edit.html', {'form': form})
    else:
        form = OrgaoForm()
        return render(request, 'orgao_edit.html', {'form': form})

@login_required
@admin_required
def orgao_delete(request, id):
    try:
        Orgao.objects.filter(pk=id).delete()
        return redirect("orgao")
    except Exception as e:
        print(e)
        orgaos = Orgao.objects.all()
        return render(request, 'deleteError.html', {'url': 'orgao.html', 'orgaos': orgaos})

@login_required
@admin_required
def orgao_invisible(request, id):
    Orgao.objects.filter(pk=id).update(ind_excluido=1)
    return redirect("orgao")

@login_required
@admin_required
def orgao_visible(request, id):
    Orgao.objects.filter(pk=id).update(ind_excluido=0)
    return redirect("orgao")

@login_required
@admin_required
def gestores_orgao(request, pk):
    if hasattr(request.user, 'profile'):
        orgao_escolhido = Orgao.objects.get(pk=pk)
        if request.method == "POST":
            profile = Profile.objects.get(pk=request.POST['usuario'])
            profile.orgao_ativo = Orgao.objects.get(pk=pk)
            profile.save()
            profile.orgaos.add(pk)

        profiles_orgao = Profile.objects.filter(orgaos=pk)
        profiles = Profile.objects.exclude(orgaos=pk)
        users = User.objects.all()
        return render(request, 'gestores_orgao.html', {'users': users,
                                                       'profiles': profiles,
                                                       'profiles_orgao': profiles_orgao,
                                                       'orgao_escolhido': orgao_escolhido})
    else:
        return redirect('error')
