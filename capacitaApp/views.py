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
from django.db import connection


# Para importação
from copy import deepcopy

@login_required
def mudanca_orgao(request, pk):
    profile = Profile.objects.get(user=request.user)
    if profile.orgaos.get(pk = pk):
        profile.orgao_ativo = Orgao.objects.get(cod_orgao = pk)
        profile.save()
        return redirect('/')
    else:
        return render(request, 'error.html')


@login_required
def home(request):
    try:
        usuario = User.objects.get(id = request.user.id)
        orgao = Profile.objects.get(user=usuario).orgao_ativo
        planos_habilitados = Plano_Capacitacao.objects.filter(plano_habilitado = True) 
        if profile.user.last_login == None:
            profile = Profile.objects.create(user_id = request.user.id)
            profile.save()
        try:
            necessidade_orgao = Necessidade_Orgao.objects.all().get(cod_plano_capacitacao = planos_habilitados[0].cod_plano_capacitacao, cod_orgao = orgao)
            pode_registrar_demandas = True
        except Exception as e:
            pode_registrar_demandas = False
        
        cursor = connection.cursor()
        cursor.callproc("funHTMLSituacaoPedidoCapacitacao", (orgao.nome,))
        htmlsituacao_tmp = cursor.fetchone()[0];
        cursor.close()

        htmlsituacao = """
            <div class="espacamento40PC"><div class="rowCirculos"><center>
            """;
        setores = htmlsituacao_tmp.split('|');
        
        situacao_primeiro = ''
        existe_green = False;
        for setor in setores:
            sigla_setor = setor.split('-')[0]
            situacao = setor.split('-')[1]    
            
            if(not situacao_primeiro):
                situacao_primeiro = situacao
            else:
                if (not existe_green and situacao == 'green'):
                    existe_green = True;

            if (situacao != 'green'):
                ind_bloqueio = True;


            imagemSemCor = '';
            if( situacao != 'green'):
                imagemSemCor = 'imagemSemCor'
            
            htmlsituacao = htmlsituacao + \
                    '<div class="componenteCirculoComSeta">'+ \
                    '    <div class="divCirculoLegendaLinha">'+ \
                    '        <div>'+ \
                    '            <div class="circulo circuloVerde ' + imagemSemCor + '">'+ \
                    '            </div>'+ \
                    '            <div class="legendaSetor ">'+ \
                    '                <h2>' + sigla_setor + '</h2>'+ \
                    '            </div>'+ \
                    '        </div>'+ \
                    '    </div>'+ \
                    '    <div class="setaIndicadoraContainer">'+ \
                    '        <img class="setaIndicadora imagemSemCor" src="https://cdn3.iconfinder.com/data/icons/signs-symbols-5/126/slice331-256.png">'+ \
                    '    </div>'+ \
                    '</div>';
            
        htmlsituacao = htmlsituacao + \
            '    <div class="componenteCirculoComSeta">'+ \
            '        <div class="divCirculoLegendaLinha">'+ \
            '            <div>'+ \
            '                <div>'+ \
            '                    <img src="https://yt3.ggpht.com/a/AGF-l7_xvHq80BYmUfpfKvUFu5d_lOPTjNLlUwWSzg=s288-c-k-c0xffffffff-no-rj-mo" class="imgILB ' + imagemSemCor + '">'+ \
            '                </div>'+ \
            '                <div class="legendaSetor">'+ \
            '                    <h2>ILB</h2>'+ \
            '                </div>'+ \
            '            </div>'+ \
            '        </div>'+ \
            '        <div class="setaIndicadoraContainer">'+ \
            '            <img class="tickCorreto ' + imagemSemCor + '" src="https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Tick_Mark_Dark-512.png">'+ \
            '        </div>'+ \
            '    </div>';

        if imagemSemCor:
            htmlsituacao = htmlsituacao + \
                '   <div class="alerta">Atenção: o prazo para envio de demandas ao ILB se encerra em 18/10/2019</div>'
        else:
            htmlsituacao = htmlsituacao + \
                '   <div class="sucesso">As demandas de capacitação foram encaminhadas com sucesso ao ILB!</div>'
        
        htmlsituacao = htmlsituacao + '<center></div></div>';

            # '        <div class="fl propertiesLegenda marginLeftRow">'+ \
            # '            <div class="fl miniCirculoLegendaBranco"></div><div class="fl">Não Iniciado</div>'+ \
            # '            <div class="fl miniCirculoLegenda circuloAmarelo"></div><div class="fl">Em Andamento</div>'+ \
            # '            <div class="fl miniCirculoLegenda circuloVerde"></div><div class="fl">Enviado Para Superior</div>'+ \
            # '            <div class="fl miniCirculoLegenda circuloVermelho"></div><div class="fl">Impedido</div>'+ \
            # '        </div>'+ \


        #profile = Profile.objects.create(user_id = request.user.id)
        #profile.save()
        ind_bloqueio = (situacao_primeiro != 'green' and existe_green);
        return render(request, 'home.html', {'plano_habilitado': pode_registrar_demandas, 'ind_bloqueio' : ind_bloqueio ,
            'estado': necessidade_orgao.estado, 'orgao': orgao, 'htmlsituacao': htmlsituacao})
    except Exception as e:
        pode_registrar_demandas = False;
        print(e)
        return render(request, 'error.html')


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

@login_required
def perguntas_frequentes(request):
    return render(request, 'perguntas_frequentes.html')

@login_required
def manual(request):
    return render(request, 'manual.html')
    