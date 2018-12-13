# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Avg, Max, Count, Sum
from django.contrib.auth.decorators import login_required

import xlsxwriter
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

from capacitaApp.views import *
from plano.views import *

# Para importação
from copy import deepcopy

@login_required
def necessidade(request):
    if (hasattr(request.user, 'profile')):
        usuario = User.objects.get(id = request.user.id)
        orgao = Profile.objects.get(user=usuario)
        planos_habilitados = Plano_Capacitacao.objects.filter(plano_habilitado = True)
        necessidade_orgao = Necessidade_Orgao.objects.all().get(cod_plano_capacitacao = planos_habilitados[0].cod_plano_capacitacao, cod_orgao = orgao.orgao_id)
        gestor = is_gestor(request)
        admin = is_admin(request)

        #Caso o orgão já tenha enviado o pedido para o orgão superior
        if (necessidade_orgao.estado == True):
            return render(request, 'plano_fechado.html', { 'is_admin' : admin, 'is_gestor': gestor})
        else:
            orgao_object = Orgao.objects.get(cod_orgao = orgao.orgao_id)
            superior = None
            if orgao_object.cod_superior:
                superior = Orgao.objects.get(cod_orgao = orgao_object.cod_superior.cod_orgao)

            subordinados = Orgao.objects.all().filter(cod_superior = orgao.orgao_id)
            necessidade_subordinados = Necessidade_Orgao.objects.all().filter(cod_orgao__in = subordinados, cod_plano_capacitacao = planos_habilitados[0].cod_plano_capacitacao)
            subordinados_status = []
            for subordinado in subordinados:
                necessidade_subordinado = necessidade_subordinados.get(cod_orgao = subordinado)
                subordinados_status.append({'nome': subordinado.nome, 'estado': necessidade_subordinado.estado, 'cod_necessidade_orgao': necessidade_subordinado.cod_necessidade_orgao, 'importado': necessidade_subordinado.importado})
            necessidades = Necessidade.objects.all().exclude(ind_excluido = True).filter(cod_necessidade_orgao = necessidade_orgao.cod_necessidade_orgao)

            # Quem não é admin vê apenas os pedidos registrados em nome do órgão para o qual está autorizado
            if(gestor):
                return render(request, 'necessidade.html',
                    {'necessidades' : necessidades, 'is_admin' : admin, 'is_gestor': gestor, 'subordinados': subordinados_status, 'superior': superior})
            else:
                return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')

@login_required
def necessidade_show(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    gestor = is_gestor(request)
    admin = is_admin(request)
    gestor_orgao = True
    usuario = User.objects.get(id = request.user.id)
    orgao = Profile.objects.get(user=usuario).orgao_id
    if orgao != necessidade.cod_necessidade_orgao.cod_orgao.cod_orgao:
        gestor_orgao = False
    if request.method == 'GET':
        if (gestor_orgao):
            return render(request, 'necessidade_show.html', {'necessidade' : necessidade, 'is_admin' : admin, 'is_gestor': gestor})
        else:
            return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})
    elif request.method == 'POST' and gestor_orgao:
        necessidade = Necessidade.objects.get(cod_necessidade = pk)
        if request.POST['aprovado'] == 'True':
            necessidade.aprovado = True
        else:
            necessidade.aprovado = False
        necessidade.save()
        return redirect('/necessidade/' + pk + '/show')

@login_required
def necessidade_new(request):
    if (hasattr(request.user, 'profile')):
        admin = is_admin(request)
        gestor= is_gestor(request)
        usuario = User.objects.get(id = request.user.id)
        orgao = Profile.objects.get(user=usuario).orgao_id
        planos_habilitados = Plano_Capacitacao.objects.filter(plano_habilitado = True)

        if(planos_habilitados.count() > 0 and gestor):
            if request.method == "POST":
                data = request.POST.copy()
                form = NecessidadeForm(request.POST)
                if form.is_valid():
                    necessidade = form.save(commit=False)
                    necessidade.cod_tipo_treinamento = Tipo_Treinamento.objects.get(cod_tipo_treinamento = request.POST['tipo_treinamento'])
                    necessidade.cod_modalidade = Modalidade_Treinamento.objects.get(cod_modalidade = request.POST['modalidade'])
                    necessidade.cod_nivel = Nivel.objects.get(cod_nivel = request.POST['nivel'])
                    necessidade.treinamento = Treinamento.objects.get(cod_treinamento = request.POST.get('treinamento'))
                    necessidade.txt_descricao = request.POST.get('txt_descricao', None)
                    necessidade.cod_usuario = usuario
                    necessidade.cod_area_conhecimento = Area_Conhecimento.objects.get(pk=request.POST['area_conhecimento'])
                    necessidade.cod_objetivo_treinamento = Objetivo_Treinamento.objects.get(pk=request.POST['objetivo_treinamento'])
                    necessidade_orgao = Necessidade_Orgao.objects.all().get(cod_plano_capacitacao = planos_habilitados[0].cod_plano_capacitacao, cod_orgao = orgao)
                    necessidade.cod_necessidade_orgao = necessidade_orgao
                    if request.POST['treinamento'] == '-1' and request.POST['txt_descricao']:
                        necessidade.txt_descricao = request.POST['txt_descricao']
                    elif request.POST['treinamento'] == '-1':
                        return render(request, 'necessidade_edit.html', {'form': form, 'erro_sugestao': "Preencha o campo de sugestão!"})
                    #     treinamento_sugerido = Treinamento(cod_area_conhecimento = request.POST['area_conhecimento'], nome = request.POST['txt_descricao'], sugestao = True)
                    #     treinamento_sugerido.save()
                    else:
                        necessidade.cod_treinamento = Treinamento.objects.get(pk=request.POST['treinamento'])

                    necessidade.save()
                    return redirect('necessidade')
                else:
                    print("FOI", form.errors)
                return render(request, 'necessidade_edit.html', {'form': form})
            else:
                form = NecessidadeForm()

                if (gestor):
                    return render(request, 'necessidade_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})
                else:
                    return render(request, 'necessidade_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})
        else:
            return render(request, 'necessidade_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})
    else:
        #return render(request, 'necessidade_edit.html', {'form': form})
        return redirect('error')


@login_required
def necessidade_edit(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    necessidade_updated = {
        'treinamento': necessidade.cod_treinamento.cod_treinamento,
        'nivel': necessidade.cod_nivel.cod_nivel,
        'area_conhecimento': necessidade.cod_area_conhecimento.cod_area_conhecimento,
        'modalidade': necessidade.cod_modalidade.cod_modalidade,
        'hor_duracao': necessidade.hor_duracao,
        'tipo_treinamento': necessidade.cod_tipo_treinamento.cod_tipo_treinamento,
        'cod_prioridade': necessidade.cod_prioridade.cod_prioridade,
        'qtd_servidor': necessidade.qtd_servidor,
        'objetivo_treinamento': necessidade.cod_objetivo_treinamento.cod_objetivo_treinamento,
        'justificativa': necessidade.justificativa
    }
    treinamentos = Treinamento.objects.all().exclude(ind_excluido = True)
    usuario = User.objects.get(id = request.user.id)
    admin = is_admin(request)
    gestor = is_gestor(request)
    gestor_orgao = True
    areas = Area_Conhecimento.objects.all().exclude(ind_excluido = True)
    orgao = Profile.objects.get(user=usuario).orgao_id
    if orgao != necessidade.cod_necessidade_orgao.cod_orgao.cod_orgao:
        gestor_orgao = False

    planos_habilitados = Plano_Capacitacao.objects.filter(plano_habilitado = True);

    if (gestor_orgao):
        if request.method == "POST":
            form = NecessidadeForm(request.POST, instance=necessidade)
            if form.is_valid():
                necessidade = form.save(commit=False)
                necessidade.cod_tipo_treinamento = Tipo_Treinamento.objects.get(cod_tipo_treinamento = request.POST['tipo_treinamento'])
                necessidade.cod_modalidade = Modalidade_Treinamento.objects.get(cod_modalidade = request.POST['modalidade'])
                necessidade.cod_nivel = Nivel.objects.get(cod_nivel = request.POST['nivel'])
                necessidade.cod_treinamento = Treinamento.objects.get(cod_treinamento = request.POST['treinamento'])
                necessidade.txt_descricao = request.POST.get('txt_descricao', None)
                necessidade.cod_usuario = usuario
                necessidade_orgao = Necessidade_Orgao.objects.all().get(cod_plano_capacitacao = planos_habilitados[0].cod_plano_capacitacao, cod_orgao = orgao)
                necessidade.cod_necessidade_orgao = necessidade_orgao
                necessidade.cod_area_conhecimento = Area_Conhecimento.objects.get(pk=request.POST['area_conhecimento'])
                necessidade.cod_objetivo_treinamento = Objetivo_Treinamento.objects.get(pk=request.POST['objetivo_treinamento'])
                if request.POST['treinamento'] == '-1' and request.POST['txt_descricao']:
                    necessidade.txt_descricao = request.POST['txt_descricao']
                necessidade.save()
                return redirect('necessidade')
        else:
            form = NecessidadeForm(necessidade_updated, instance=necessidade)
        return render(request, 'necessidade_edit.html', {'form': form, 'areas' : areas, 'planos_habilitados' : planos_habilitados, 'necessidade' : necessidade, 'treinamentos' : treinamentos, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def necessidade_delete(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    gestor_orgao = True
    usuario = User.objects.get(id = request.user.id)
    orgao = Profile.objects.get(user=usuario).orgao_id
    if orgao != necessidade.cod_necessidade_orgao.cod_orgao.cod_orgao:
        gestor_orgao = False

    admin = is_admin(request)
    gestor = is_gestor(request)
    if gestor_orgao:
        necessidade.ind_excluido = 1
        necessidade.save()
        return redirect("necessidade")
    else:
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})

def necessidade_approve(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if (admin):
        necessidade = get_object_or_404(Necessidade, pk=pk)
        necessidade.aprovado = False
        necessidade.save()
        return redirect("necessidade")
    else:
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})

def necessidade_disapprove(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if (admin):
        necessidade = get_object_or_404(Necessidade, pk=pk)
        necessidade.aprovado = True
        necessidade.save()
        return redirect("necessidade")
    else:
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})

def necessidade_orgao_close(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if (admin):
        necessidade_orgao = get_object_or_404(Necessidade_Orgao, pk=pk)
        necessidade_orgao.estado = True
        necessidade_orgao.save()
        return redirect("necessidade")
    else:
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})

def importar_necessidade(request, pk, pk_atual):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if (admin):
        necessidade_orgao = get_object_or_404(Necessidade_Orgao, pk=pk)
        necessidade_orgao.importado = True
        necessidade_orgao.save()
        print("ORGAO = ", necessidade_orgao.importado)
        print("ORGAO = ", necessidade_orgao.cod_necessidade_orgao)

        necessidades = Necessidade.objects.all().filter(cod_necessidade_orgao = necessidade_orgao.cod_necessidade_orgao)
        for necessidade in necessidades:
            necessidade_importada = deepcopy(necessidade)
            necessidade_importada.cod_necessidade = None
            necessidade_importada.cod_necessidade_orgao = Necessidade_Orgao.objects.get(cod_necessidade_orgao = pk_atual)
            necessidade_importada.save()
        return redirect("necessidade")
    else:
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})
