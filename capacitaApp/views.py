# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Avg, Max, Count, Sum
from django.contrib.auth.decorators import login_required

import xlsxwriter
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from .filters import *
from .filtro_necessidade import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

def is_admin(request):
    user = User.objects.get(id = request.user.id)
    relacoes = AuthUserGroups.objects.all()
    for relacao in relacoes:
        if relacao.user_id == user.id and relacao.group_id == 1:
            return True
    return False

def is_gestor(request):
    user = User.objects.get(id = request.user.id)
    relacoes = AuthUserGroups.objects.all()
    for relacao in relacoes:
        if relacao.user_id == user.id and relacao.group_id == 2:
            return True
    return False


@login_required
def home(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    return render(request, 'capacita/home.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def plano(request):
    planos = Plano_Capacitacao.objects.all()
    form = PlanoForm()
    admin = is_admin(request)
    gestor = is_gestor(request)

    if admin:
        return render(request, 'capacita/plano_capacitacao.html', {'planos' : planos, 'form' : form, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def plano_delete(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if (admin):
        plano = get_object_or_404(Plano_Capacitacao, pk=pk)
        plano.ind_excluido = 1
        plano.save()
        return redirect("plano")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def plano_undelete(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if (admin):
        plano = get_object_or_404(Plano_Capacitacao, pk=pk)
        plano.ind_excluido = 0
        plano.save()
        return redirect("plano")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})


@login_required
def plano_show(request, id):
    admin = is_admin(request)
    gestor = is_gestor(request)
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    if admin:
        return render(request, 'capacita/plano_show.html', {'plano' : plano})
    else:
        return redirect('error')

@login_required
def plano_new(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if request.method == "POST":
        form = PlanoForm(request.POST)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.save()
            return redirect('plano')
    else:
        form = PlanoForm()
    if(admin):
        return render(request, 'capacita/plano_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')

@login_required
def plano_edit(request, id):
    admin = is_admin(request)
    gestor = is_gestor(request)
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    if request.method == "POST":
        form = PlanoForm(request.POST, instance=plano)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.save()
            return redirect("plano")
    else:
        form = PlanoForm(instance=plano)
    if(admin):
        return render(request, 'capacita/plano_edit.html', {'form' : form, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')

@login_required
def necessidade(request):
    if (hasattr(request.user, 'profile')):
        areas = Area_Conhecimento.objects.all().exclude(ind_excluido = True)
        niveis = Nivel.objects.all().exclude(ind_excluido = True)
        planos = Plano_Capacitacao.objects.all().exclude(ind_excluido = True)
        gestor = is_gestor(request)
        admin = is_admin(request)
        gestor_orgao = True

        profile_usuario = Profile.objects.get(user_id = request.user.id)
        orgao_usuario = Orgao.objects.get(cod_orgao=profile_usuario.orgao_id)

        area = False;
        plano = False;
        nivel = False;
        turno = False;
        qtd_servidor = False;

        if  request.GET.get('area'):
            area = request.GET.get('area')
        if  request.GET.get('nivel'):
            nivel = request.GET.get('nivel')
        if  request.GET.get('qtd_servidor'):
            qtd_servidor = request.GET.get('qtd_servidor')

        necessidades = Necessidade.objects.all().exclude(ind_excluido = True)
        necessidades = necessidades.filter(cod_orgao = request.user.profile.orgao_id)

        # Quem não é admin vê apenas os pedidos registrados em nome do órgão para o qual está autorizado
        if(gestor):
            return render(request, 'capacita/necessidade.html',
                {'necessidades' : necessidades, 'areas' : areas, 'niveis' : niveis, 'planos' : planos,
                 'orgao_usuario' : orgao_usuario, 'is_admin' : admin, 'is_gestor': gestor})
        else:
            return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
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
    if orgao != necessidade.cod_orgao.cod_orgao:
        gestor_orgao = False
    if request.method == 'GET':
        if (gestor_orgao):
            return render(request, 'capacita/necessidade_show.html', {'necessidade' : necessidade, 'is_admin' : admin, 'is_gestor': gestor})
        else:
            return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
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
        areas = Area_Conhecimento.objects.all().exclude(ind_excluido = True)
        treinamentos = Treinamento.objects.all().exclude(ind_excluido = True)
        usuario = User.objects.get(id = request.user.id)
        admin = is_admin(request)
        gestor= is_gestor(request)
        usuario = User.objects.get(id = request.user.id)
        orgao = Profile.objects.get(user=usuario).orgao_id
        planos_habilitados = Plano_Capacitacao.objects.filter(plano_habilitado = True)
        # if(request.POST['txt_descricao'] != ''):

        if(planos_habilitados.count() > 0 and gestor):
            if request.method == "POST":
                data = request.POST.copy()
                form = NecessidadeForm(request.POST)
                if form.is_valid():
                    necessidade = form.save(commit=False)
                    necessidade.cod_plano_capacitacao = planos_habilitados[0]
                    necessidade.cod_tipo_treinamento = Tipo_Treinamento.objects.get(cod_tipo_treinamento = request.POST['tipo_treinamento'])
                    necessidade.cod_modalidade = Modalidade_Treinamento.objects.get(cod_modalidade = request.POST['modalidade'])
                    necessidade.cod_orgao = Orgao.objects.get(cod_orgao=orgao)
                    necessidade.cod_nivel = Nivel.objects.get(cod_nivel = request.POST['nivel'])
                    necessidade.treinamento = Treinamento.objects.get(cod_treinamento = request.POST.get('treinamento'))
                    necessidade.txt_descricao = request.POST.get('txt_descricao', None)
                    necessidade.cod_usuario = usuario
                    necessidade.cod_area_conhecimento = Area_Conhecimento.objects.get(pk=request.POST['area_conhecimento'])
                    necessidade.cod_objetivo_treinamento = Objetivo_Treinamento.objects.get(pk=request.POST['objetivo_treinamento'])
                    if request.POST['treinamento'] == '-1' and request.POST['txt_descricao']:
                        necessidade.txt_descricao = request.POST['txt_descricao']
                    elif request.POST['treinamento'] == '-1':
                        return render(request, 'capacita/necessidade_edit.html', {'form': form, 'erro_sugestao': "Preencha o campo de sugestão!"})
                    #     treinamento_sugerido = Treinamento(cod_area_conhecimento = request.POST['area_conhecimento'], nome = request.POST['txt_descricao'], sugestao = True)
                    #     treinamento_sugerido.save()
                    else:
                        necessidade.cod_treinamento = Treinamento.objects.get(pk=request.POST['treinamento'])

                    necessidade.save()
                    return redirect('necessidade')
                else:
                    print("FOI", form.errors)
                return render(request, 'capacita/necessidade_edit.html', {'form': form})
            else:
                form = NecessidadeForm()

                if (gestor):
                    return render(request, 'capacita/necessidade_edit.html', {'form': form, 'areas' : areas, 'eh_necessidade' : False, 'planos_habilitados' : planos_habilitados, 'treinamentos' : treinamentos, 'is_admin': admin, 'is_gestor': gestor})
                else:
                    return render(request, 'capacita/necessidade_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})
        else:
            return render(request, 'capacita/necessidade_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})
    else:
        #return render(request, 'capacita/necessidade_edit.html', {'form': form})
        return redirect('error')


@login_required
def necessidade_edit(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    necessidade_updated = {
        'treinamento': necessidade.cod_treinamento.cod_treinamento,
        'nivel': necessidade.cod_nivel.cod_nivel,
        'area_conhecimento': necessidade.cod_area_conhecimento.cod_area_conhecimento,
        'cod_evento': necessidade.cod_evento.cod_evento,
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
    if orgao != necessidade.cod_orgao.cod_orgao:
        gestor_orgao = False

    planos_habilitados = Plano_Capacitacao.objects.filter(plano_habilitado = True);

    if (gestor_orgao):
        if request.method == "POST":
            form = NecessidadeForm(request.POST, instance=necessidade)
            if form.is_valid():
                necessidade = form.save(commit=False)
                necessidade.cod_plano_capacitacao = planos_habilitados[0]
                necessidade.cod_tipo_treinamento = Tipo_Treinamento.objects.get(cod_tipo_treinamento = request.POST['tipo_treinamento'])
                necessidade.cod_modalidade = Modalidade_Treinamento.objects.get(cod_modalidade = request.POST['modalidade'])
                necessidade.cod_orgao = Orgao.objects.get(cod_orgao=orgao)
                necessidade.cod_nivel = Nivel.objects.get(cod_nivel = request.POST['nivel'])
                necessidade.cod_treinamento = Treinamento.objects.get(cod_treinamento = request.POST['treinamento'])
                necessidade.txt_descricao = request.POST.get('txt_descricao', None)
                necessidade.cod_usuario = usuario
                necessidade.cod_area_conhecimento = Area_Conhecimento.objects.get(pk=request.POST['area_conhecimento'])
                necessidade.cod_objetivo_treinamento = Objetivo_Treinamento.objects.get(pk=request.POST['objetivo_treinamento'])
                if request.POST['treinamento'] == '-1' and request.POST['txt_descricao']:
                    necessidade.txt_descricao = request.POST['txt_descricao']
                necessidade.save()
                return redirect('necessidade')
        else:
            form = NecessidadeForm(necessidade_updated, instance=necessidade)
        return render(request, 'capacita/necessidade_edit.html', {'form': form, 'areas' : areas, 'planos_habilitados' : planos_habilitados, 'necessidade' : necessidade, 'treinamentos' : treinamentos, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def necessidade_delete(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    gestor_orgao = True
    usuario = User.objects.get(id = request.user.id)
    orgao = Profile.objects.get(user=usuario).orgao_id
    if orgao != necessidade.cod_orgao.cod_orgao:
        gestor_orgao = False

    admin = is_admin(request)
    gestor = is_gestor(request)
    if gestor_orgao:
        necessidade.ind_excluido = 1
        necessidade.save()
        return redirect("necessidade")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def treinamentos(request):
    treinamentos = Treinamento.objects.all().exclude(pk=-1)
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        return render(request, 'capacita/treinamento.html', {'treinamentos' : treinamentos, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def treinamento_edit(request, pk):
    treinamento = get_object_or_404(Treinamento, pk=pk)
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin and request.method == "POST":
        form = TreinamentoForm(request.POST, instance=treinamento)
        if form.is_valid():
            treinamento = form.save(commit=False)
            treinamento.save()
            return redirect('treinamentos')
    elif request.method != "POST" and admin:
        form = TreinamentoForm(instance=treinamento)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/treinamento_edit.html', {'form': form, 'is_admin':admin, 'is_gestor': gestor})

@login_required
def treinamento_new(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin and request.method == "POST":
        form = TreinamentoForm(request.POST)
        if form.is_valid():
            treinamento = form.save(commit=False)
            treinamento.save()
            return redirect('treinamentos')
    elif request.method != "POST" and admin:
        form = TreinamentoForm()
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/treinamento_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})

@login_required
def treinamento_delete(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        treinamento = get_object_or_404(Treinamento, pk=pk)
        treinamento.ind_excluido = True
        treinamento.save()
        return redirect("treinamentos")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def treinamento_undelete(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        treinamento = get_object_or_404(Treinamento, pk=pk)
        treinamento.ind_excluido = False
        treinamento.save()
        return redirect("treinamentos")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def objetivos(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        objetivos = Objetivo_Treinamento.objects.all()
        return render(request, 'capacita/objetivos.html', {'objetivos' : objetivos, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def objetivo_edit(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    objetivo = get_object_or_404(Objetivo_Treinamento, pk=pk)
    if request.method == "POST" and admin:
        form = ObjetivoTreinamentoForm(request.POST, instance=objetivo)
        if form.is_valid():
            objetivo = form.save(commit=False)
            objetivo.save()
            return redirect('objetivos')
    elif request.method != "POST" and admin:
        form = ObjetivoTreinamentoForm(instance=objetivo)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/objetivo_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})

@login_required
def objetivo_new(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if request.method == "POST" and admin:
        form = ObjetivoTreinamentoForm(request.POST)
        if form.is_valid():
            objetivo = form.save(commit=False)
            objetivo.save()
            return redirect('objetivos')
    elif request.method != "POST" and admin:
        form = ObjetivoTreinamentoForm()
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/objetivo_edit.html', {'form': form})

@login_required
def objetivo_delete(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        objetivo = get_object_or_404(Objetivo_Treinamento, pk=pk)
        objetivo.ind_excluido = 1
        objetivo.save()
        return redirect("objetivos")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def objetivo_undelete(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        objetivo = get_object_or_404(Objetivo_Treinamento, pk=pk)
        objetivo.ind_excluido = 0
        objetivo.save()
        return redirect("objetivos")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def orgao(request):
    if (hasattr(request.user, 'profile')):
        orgaos_list = Orgao.objects.all()
        page = request.GET.get('page', 1)
        admin = is_admin(request)
        gestor = is_gestor(request)
        paginator = Paginator(orgaos_list, 10)
        permissao = False
        paginator = Paginator(orgaos_list, 6)
        if admin:
            try:
                orgaos = paginator.page(page)
            except PageNotAnInteger:
                orgaos = paginator.page(1)
            except EmptyPage:
                orgaos = paginator.page(paginator.num_pages)
            return render(request, 'capacita/orgao.html', {'orgaos' : orgaos, 'is_admin' : admin, 'is_gestor': gestor})
        else:
            return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')

@login_required
def orgao_edit(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    orgao = get_object_or_404(Orgao, pk=pk)
    if request.method == "POST" and admin:
        form = OrgaoForm(request.POST, instance=orgao)
        if form.is_valid():
            orgao = form.save(commit=False)
            orgao.save()
            return redirect('orgao')
    elif request.method != "POST" and admin:
        form = OrgaoForm(instance=orgao)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/orgao_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})

@login_required
def orgao_new(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if request.method == "POST" and admin:
        form = OrgaoForm(request.POST)
        if form.is_valid():
            orgao = form.save(commit=False)
            orgao.save()
            return redirect('orgao')
    elif request.method != "POST" and admin:
        form = OrgaoForm()
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/orgao_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})

@login_required
def orgao_delete(request, id):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        orgao = Orgao.objects.filter(pk=id).update(ind_excluido=1)
        return redirect("orgao")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def orgao_undelete(request, id):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        orgao = Orgao.objects.filter(pk=id).update(ind_excluido=0)
        return redirect("orgao")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def tipos_treinamento(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    tipos = Tipo_Treinamento.objects.all()
    if admin:
        return render(request, 'capacita/tipo_treinamento.html', {'tipos' : tipos, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def tipo_treinamento_delete(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        tipo = get_object_or_404(Tipo_Treinamento, pk=pk)
        tipo.ind_excluido = 1
        print (tipo.ind_excluido)
        tipo.save()
        print ("salvo!")
        return redirect("tipos_treinamento")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def tipo_treinamento_undelete(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        tipo = get_object_or_404(Tipo_Treinamento, pk=pk)
        tipo.ind_excluido = 0
        tipo.save()
        return redirect("tipos_treinamento")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def tipo_treinamento_edit(request,id):
    tipo = get_object_or_404(Tipo_Treinamento, pk=id)
    admin = is_admin(request)
    gestor = is_gestor(request)
    if request.method == 'POST' and admin:
        form = TipoTreinamentoForm(request.POST, instance=tipo, initial={'ind_excluido' : 0})
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect("tipos_treinamento")
    elif request.method != 'POST':
        form = TipoTreinamentoForm(instance=tipo)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/tipo_treinamento_edit.html', {'form' : form, 'is_admin': admin, 'is_gestor': gestor})

@login_required
def tipo_treinamento_new(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if request.method == 'POST':
        form = TipoTreinamentoForm(request.POST)
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect("tipos_treinamento")
    elif request.method != 'POST':
        form = TipoTreinamentoForm()
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/tipo_treinamento_edit.html', {'form' : form, 'is_admin': admin, 'is_gestor': gestor})

@login_required
def relatorio(request):
    admin = is_admin(request)
    gestor = is_gestor(request)

    if admin:
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('Necessidades.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.set_column(0, 9, 20)
        worksheet.set_column(4, 4, 40)

        bold = workbook.add_format({'bold': True, 'center_across' : True})
        center = workbook.add_format({'center_across' : True})


        necessidades = Necessidade.objects.all().exclude(ind_excluido = True)
        # .values('treinamento', 'txt_descricao', 'aprovado').annotate(
        #     cod_necessidade=Max('cod_necessidade'),qtd_servidor=Sum('qtd_servidor'),
        #     hor_duracao= Avg('hor_duracao'),cod_prioridade=Avg('cod_prioridade_id'),
        #     cod_plano_capacitacao=Avg('cod_plano_capacitacao_id'),  cod_usuario=Avg('cod_usuario_id'),
        #     cod_nivel=Avg('cod_nivel_id'),cod_evento=Avg('cod_evento_id')
        # )

        necessidades = necessidades.filter(ind_excluido = 0)


        row = 0
        col = 0

        worksheet.write(row, col,         "PCASF", bold)
        worksheet.write(row, col + 1,     "Órgão", bold)
        worksheet.write(row, col + 2,     "Área de Conhecimento", bold)
        worksheet.write(row, col + 3,     "Treinamento", bold)
        worksheet.write(row, col + 4,     "Evento", bold)
        worksheet.write(row, col + 5,     "Modalidade", bold)
        worksheet.write(row, col + 6,     "Nível", bold)
        worksheet.write(row, col + 7,     "Carga Horária", bold)
        worksheet.write(row, col + 8,     "Tipo de Treinamento", bold)
        worksheet.write(row, col + 9,     "Prioridade", bold)
        worksheet.write(row, col + 10,     "Quantidade de Servidores", bold)
        worksheet.write(row, col + 11,     "Objetivo", bold)
        worksheet.write(row, col + 12,     "Justificativa", bold)

        row += 1

        for necessidade in necessidades:

            print (necessidade.cod_treinamento)

            if (necessidade.cod_treinamento.cod_treinamento == -1):
                treinamento = necessidade.txt_descricao
            else:
                treinamento = Treinamento.objects.get(cod_treinamento=necessidade.cod_treinamento.cod_treinamento).nome

            worksheet.write(row, col,     necessidade.cod_plano_capacitacao.ano_plano_capacitacao, center)
            worksheet.write(row, col + 1, necessidade.cod_orgao.nome, center)
            worksheet.write(row, col + 2, necessidade.cod_area_conhecimento.txt_descricao, center)
            worksheet.write(row, col + 3, treinamento, center)
            worksheet.write(row, col + 4, necessidade.cod_evento.nome, center)
            #Evento.objects.get(cod_evento=necessidade['cod_evento']).nome, center)
            worksheet.write(row, col + 5, necessidade.cod_modalidade.nome, center)
            worksheet.write(row, col + 6, Nivel.objects.get(cod_nivel=necessidade.cod_nivel.cod_nivel).nome, center)
            worksheet.write(row, col + 7, necessidade.hor_duracao, center)
            worksheet.write(row, col + 8, necessidade.cod_tipo_treinamento.cod_tipo_treinamento, center)
            worksheet.write(row, col + 9, Prioridade.objects.get(cod_prioridade=necessidade.cod_prioridade.cod_prioridade).nome, center)
            worksheet.write(row, col + 10, necessidade.qtd_servidor, center)
            worksheet.write(row, col + 11, Objetivo_Treinamento.objects.get(cod_objetivo_treinamento=necessidade.cod_objetivo_treinamento.cod_objetivo_treinamento).nome, center)
            worksheet.write(row, col + 12, necessidade.justificativa, center)

        #    if (necessidade['aprovado'] == 0):
        #        worksheet.write(row, col + 8, 'Sim', center)
        #    else:
        #        worksheet.write(row, col + 8, 'Não', center)

            row += 1

        worksheet.set_default_row(20)

        workbook.close()

        fh = open("Necessidades.xlsx", 'rb')

        response = HttpResponse(fh) # mimetype is replaced by content_type for django 1.7
        response['Content-Disposition'] = 'attachment; filename=%s' % "Necessidades.xlsx"
        response['X-Sendfile'] = fh

        return response
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def areas(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        areas = Area_Conhecimento.objects.all();
        return render(request, 'capacita/areas.html', { 'areas' : areas , 'is_admin': admin, 'is_gestor': gestor})
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def area_delete(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        area = get_object_or_404(Area_Conhecimento, pk=pk)
        area.ind_excluido = 1
        area.save()
        return redirect("areas")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def area_undelete(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        area = get_object_or_404(Area_Conhecimento, pk=pk)
        area.ind_excluido = 0
        area.save()
        return redirect("areas")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def area_edit(request,id):
    admin = is_admin(request)
    gestor = is_gestor(request)
    area = get_object_or_404(Area_Conhecimento, pk=id)
    if request.method == 'POST' and admin:
        form = AreaConhecimentoForm(request.POST, instance=area, initial={'ind_excluido' : 0})
        if form.is_valid():
            area = form.save(commit=False)
            area.save()
            return redirect("areas")
    elif request.method != 'POST':
        form = AreaConhecimentoForm(instance=area)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/area_edit.html', {'form' : form, 'is_admin': admin, 'is_gestor': gestor})

@login_required
def area_new(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if request.method == 'POST' and admin:
        form = AreaConhecimentoForm(request.POST)
        if form.is_valid():
            area = form.save(commit=False)
            area.save()
            return redirect("areas")
    elif request.method != 'POST':
        form = AreaConhecimentoForm()
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/area_edit.html', {'form' : form, 'is_admin': admin, 'is_gestor': gestor})



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
        gestor = is_gestor(request)
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

        return render(request, 'capacita/usuarios.html', {'users' : users, 'profiles' : profiles, 'orgao' : orgao, 'orgaos' : orgaos, 'is_admin': admin, 'is_gestor': gestor})
    else:
        if ((group in request.user.groups.all())):
            return render(request, 'capacita/usuarios.html', {'users' : users, 'profiles' : profiles, 'orgao' : orgao, 'is_admin': admin, 'is_gestor': gestor})
        else:
            return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@csrf_exempt
def usuarios_permissao(request):
    if request.method == "POST":
        profile = Profile.objects.filter(user_id=request.POST.get("usuario_id", "")).update(permissao_necessidade=request.POST.get("data", ""))
        if (request.POST.get("data", "") == 'True'):
            profile = Profile.objects.filter(user_id=request.POST.get("usuario_id", "")).update(permissao_necessidade=True)
        if (request.POST.get("data", "") == 'False'):
            profile = Profile.objects.filter(user_id=request.POST.get("usuario_id", "")).update(permissao_necessidade=False)
    else:
        return redirect("/")
    return HttpResponseRedirect('/usuarios/')

@login_required
def usuario_new(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if request.method == 'POST' and admin:
        form = UserForm(request.POST)
        id_group = request.POST['group']
        my_group = Group.objects.get(id=id_group)
        if form.is_valid():
            user_check = User.objects.filter(username='zequinha').count()
            if(user_check == 0):
                usuario = form.save()
                profile = Profile.objects.create(permissao_necessidade = False, orgao_id = request.POST['orgao'], user_id = usuario.id)
                usuario.is_active = True
                usuario.groups.add(my_group)
                profile.save()
                usuario.save()
            else:
                return render(request, 'capacita/usuario_edit.html', {'form' : form, 'orgaos' : orgaos, 'groups' : groups, 'usuario' : True, 'is_admin': admin, 'is_gestor': gestor})

            return redirect("usuarios")
        else:
            return render(request, 'capacita/usuario_edit.html', {'form' : form, 'is_admin': admin, 'is_gestor': gestor})
    elif request.method != 'POST':
        form = UserForm()
        orgaos = Orgao.objects.all()
        groups = Group.objects.all()
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

    orgaos = Orgao.objects.all()
    groups = Group.objects.all()

    if(admin):
        return render(request, 'capacita/usuario_edit.html', {'form' : form, 'orgaos' : orgaos, 'groups' : groups, 'usuario' : True, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')

@login_required
def usuario_edit(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
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
    if(admin):
        return render(request, 'capacita/usuario_edit.html', {'form': form, 'orgaos' : orgaos, 'groups' : groups, 'usuario' : usuario, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')

@login_required
def modalidade(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if (hasattr(request.user, 'profile')):
        modalidades = Modalidade_Treinamento.objects.all()
        return render(request, 'capacita/modalidades.html', {'modalidades' : modalidades, 'permissao' : admin, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')

@login_required
def modalidade_edit(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    modalidade = get_object_or_404(Modalidade_Treinamento, pk=pk)
    if request.method == "POST" and admin:
        form = ModalidadeForm(request.POST, instance=modalidade)
        if form.is_valid():
            modalidade = form.save(commit=False)
            modalidade.save()
            return redirect('modalidade')
    elif request.method != "POST" and admin:
        form = ModalidadeForm(instance=modalidade)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

    if(admin):
        return render(request, 'capacita/modalidade_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')

@login_required
def modalidade_new(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if request.method == "POST" and admin:
        form = ModalidadeForm(request.POST)
        if form.is_valid():
            modalidade = form.save(commit=False)
            modalidade.save()
            return redirect('modalidade')
    elif request.method != "POST" and admin:
        form = ModalidadeForm()
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/modalidade_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})

@login_required
def modalidade_delete(request, pk):
    admin = is_admin(request)
    if (admin):
        modalidade = get_object_or_404(Modalidade_Treinamento, pk=pk)
        modalidade.ind_excluido = True
        modalidade.save()
        return redirect("modalidade")
    else:
        return redirect('error')

@login_required
def modalidade_undelete(request, pk):
    admin = is_admin(request)
    if (admin):
        modalidade = get_object_or_404(Modalidade_Treinamento, pk=pk)
        modalidade.ind_excluido = False
        modalidade.save()
        return redirect("modalidade")
    else:
        return redirect('error')

@login_required
def api_areas(request):
    admin_or_gestor = is_admin(request) or is_gestor(request)
    if(admin_or_gestor):
        areas = Area_Conhecimento.objects.all().exclude(ind_excluido = True).values()
        areas = list(areas)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return JsonResponse(areas, safe=False)

@login_required
def api_cursos(request):
    admin_or_gestor = is_admin(request) or is_gestor(request)
    if(admin_or_gestor):
        treinamentos = Treinamento.objects.all().exclude(ind_excluido = True).values()
        treinamentos = list(treinamentos)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return JsonResponse(treinamentos, safe=False)

@login_required
def api_tipos_treinamento(request):
    admin_or_gestor = is_admin(request) or is_gestor(request)
    if(admin_or_gestor):
        tipos = Tipo_Treinamento.objects.all().exclude(ind_excluido = True).values()
        tipos = list(tipos)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return JsonResponse(tipos, safe=False)

@login_required
def api_planos(request):
    admin_or_gestor = is_admin(request) or is_gestor(request)
    if(admin_or_gestor):
        planos = Plano_Capacitacao.objects.all().exclude(ind_excluido = True).values()
        planos = list(planos)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return JsonResponse(planos, safe=False)

@login_required
def error(request):
    return render(request, 'capacita/error.html')

@login_required
def avaliacao_cursos(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    gestor_or_adm = is_gestor(request) or admin
    if request.method == "POST" and gestor_or_adm:
        necessidade = Necessidade.objects.get(cod_necessidade = request.POST['cod_necessidade'])
        necessidade.txt_descricao = None
        treinamento = Treinamento.objects.create(nome = request.POST['txt'], cod_area_conhecimento = necessidade.cod_area_conhecimento)
        treinamento.save()
        necessidade.treinamento = treinamento
        necessidade.save()

        return redirect('avaliacao_cursos')
    elif request.method != "POST" and admin:
        cursos_necessidades = Necessidade.objects.exclude(txt_descricao = None).exclude(txt_descricao = '')
        return render(request, "capacita/avaliacao_cursos.html", {'necessidades' : cursos_necessidades, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
