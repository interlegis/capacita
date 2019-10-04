from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import xlsxwriter
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *
from necessidade.models import *
from .forms import *
from django.http import HttpResponse
from capacita.template_context_processors import is_gestor, is_admin

# Para importação
from copy import deepcopy

@login_required
def mudanca_orgao(request, pk):
    profile = Profile.objects.get(user=request.user)
    if profile.orgaos.get(pk=pk):
        profile.orgao_ativo = Orgao.objects.get(cod_orgao=pk)
        profile.save()
        return redirect('/')
    else:
        return render(request, 'error.html')


@login_required
def home(request):
    try:
        profile = Profile.objects.create(user_id = request.user.id)
        profile.save()
    except Exception as e:
        print(e)
    return render(request, 'home.html')


@login_required
def relatorio(request):
    plano_habilitado = Plano_Capacitacao.objects.filter(plano_habilitado = True)
    orgao_id = Profile.objects.get(user=request.user).orgao_ativo_id
    orgaos = Orgao.objects.filter(cod_superior=None)
    necessidades = Necessidade.objects.none()
    for orgao in orgaos:
        try:
            necessidade_orgao = Necessidade_Orgao.objects.get(cod_orgao = orgao, cod_plano_capacitacao = plano_habilitado[0], estado=True)
            necessidades = necessidades | Necessidade.objects.all().filter(ind_excluido = False, cod_necessidade_orgao = necessidade_orgao, aprovado=True)
        except Exception as e:
            print(e)

    if not necessidades:
        return render(request, 'tabelaErro.html')
    elif is_admin(request)['is_admin']:
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('Necessidades.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.set_column(0, 9, 20)
        worksheet.set_column(4, 4, 40)

        bold = workbook.add_format({'bold': True, 'center_across' : True})
        center = workbook.add_format({'center_across' : True})

        row = 0
        col = 0

        worksheet.write(row, col,         "PCASF", bold)
        worksheet.write(row, col + 1,     "Órgão", bold)
        worksheet.write(row, col + 2,     "Área de Conhecimento", bold)
        worksheet.write(row, col + 3,     "Treinamento", bold)
        worksheet.write(row, col + 4,     "Modalidade", bold)
        worksheet.write(row, col + 5,     "Nível", bold)
        worksheet.write(row, col + 6,     "Carga Horária", bold)
        worksheet.write(row, col + 7,     "Tipo de Treinamento", bold)
        worksheet.write(row, col + 8,     "Prioridade", bold)
        worksheet.write(row, col + 9,     "Quantidade de Servidores", bold)
        worksheet.write(row, col + 10,     "Objetivo", bold)
        worksheet.write(row, col + 11,     "Justificativa", bold)

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
            worksheet.write(row, col + 4, necessidade.cod_modalidade.nome, center)
            worksheet.write(row, col + 5, Nivel.objects.get(cod_nivel=necessidade.cod_nivel.cod_nivel).nome, center)
            worksheet.write(row, col + 6, necessidade.hor_duracao, center)
            worksheet.write(row, col + 7, necessidade.cod_tipo_treinamento.cod_tipo_treinamento, center)
            worksheet.write(row, col + 8, Prioridade.objects.get(cod_prioridade=necessidade.cod_prioridade.cod_prioridade).nome, center)
            worksheet.write(row, col + 9, necessidade.qtd_servidor, center)
            worksheet.write(row, col + 10, Objetivo_Treinamento.objects.get(cod_objetivo_treinamento=necessidade.cod_objetivo_treinamento.cod_objetivo_treinamento).nome, center)
            worksheet.write(row, col + 11, necessidade.justificativa, center)

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
        return render(request, 'error.html')

@login_required
def error(request):
    return render(request, 'error.html')


@login_required
def processo_capacitacao(request):
    return render(request, 'processo_capacitacao.html')

def perguntas_frequentes(request):
    return render(request, 'perguntas_frequentes.html')

def manual(request):
    return render(request, 'manual.html')
    