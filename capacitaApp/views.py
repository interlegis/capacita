# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Avg, Max, Count, Sum
from django.contrib.auth.decorators import login_required

import xlsxwriter
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from necessidade import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

# Para importação
from copy import deepcopy

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
    return render(request, 'home.html', {'is_admin': admin, 'is_gestor': gestor})

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
        # )

        necessidades = necessidades.filter(ind_excluido = 0)


        row = 0
        col = 0

        worksheet.write(row, col,         "PCASF", bold)
        worksheet.write(row, col + 1,     "Órgão", bold)
        worksheet.write(row, col + 2,     "Área de Conhecimento", bold)
        worksheet.write(row, col + 3,     "Treinamento", bold)
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

            worksheet.write(row, col,     necessidade.cod_necessidade_orgao.cod_plano_capacitacao.ano_plano_capacitacao, center)
            worksheet.write(row, col + 1, necessidade.cod_necessidade_orgao.cod_orgao.nome, center)
            worksheet.write(row, col + 2, necessidade.cod_area_conhecimento.txt_descricao, center)
            worksheet.write(row, col + 3, treinamento, center)
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
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def error(request):
    return render(request, 'error.html')

# @login_required
# def avaliacao_cursos(request):
#     admin = is_admin(request)
#     gestor = is_gestor(request)
#     gestor_or_adm = is_gestor(request) or admin
#     if request.method == "POST" and gestor_or_adm:
#         necessidade = Necessidade.objects.get(cod_necessidade = request.POST['cod_necessidade'])
#         necessidade.txt_descricao = None
#         treinamento = Treinamento.objects.create(nome = request.POST['txt'], cod_area_conhecimento = necessidade.cod_area_conhecimento)
#         treinamento.save()
#         necessidade.treinamento = treinamento
#         necessidade.save()
#
#         return redirect('avaliacao_cursos')
#     elif request.method != "POST" and admin:
#         cursos_necessidades = Necessidade.objects.exclude(txt_descricao = None).exclude(txt_descricao = '')
#         return render(request, "avaliacao_cursos.html", {'necessidades' : cursos_necessidades, 'is_admin': admin, 'is_gestor': gestor})
#     else:
#         return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})
