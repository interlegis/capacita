from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import connection
from .models import *
from .forms import *
from capacita.template_context_processors import is_gestor, is_admin
from capacita.decorators import admin_required, gestor_required
from django.urls import reverse
from django.contrib.messages import error

@login_required
@gestor_required
def necessidade(request):
    if (hasattr(request.user, 'profile')):
        usuario = User.objects.get(id = request.user.id)
        orgao = Profile.objects.get(user=usuario).orgao_ativo
        try:
            planos_habilitados = Plano_Capacitacao.objects.filter(plano_habilitado = True)
            necessidade_orgao = Necessidade_Orgao.objects.all().get(cod_plano_capacitacao = planos_habilitados[0].cod_plano_capacitacao, cod_orgao = orgao)
            pode_registrar_demandas = True
        except Exception as e:
            planos_habilitados = Plano_Capacitacao.objects.filter(plano_habilitado = False)
            pode_registrar_demandas = False
            necessidade_orgao = Necessidade_Orgao.objects.all().get(cod_plano_capacitacao = planos_habilitados[0].cod_plano_capacitacao, cod_orgao = orgao)
            
        orgao_object = Orgao.objects.get(nome = orgao)
        superior = None
        if orgao_object.cod_superior:
            superior = Orgao.objects.get(cod_orgao = orgao_object.cod_superior.cod_orgao)

        subordinados = Orgao.objects.all().filter(cod_superior = orgao_object.cod_orgao)
        necessidade_subordinados = Necessidade_Orgao.objects.all().filter(cod_orgao__in = subordinados, cod_plano_capacitacao = planos_habilitados[0].cod_plano_capacitacao)
        subordinados_status = []
        for subordinado in subordinados:
            necessidade_subordinado = necessidade_subordinados.get(cod_orgao = subordinado)
            subordinados_status.append({'nome': subordinado.nome, 'estado': necessidade_subordinado.estado, 'cod_necessidade_orgao': necessidade_subordinado.cod_necessidade_orgao, 'cod_orgao':  subordinado.cod_orgao,'importado': necessidade_subordinado.importado})
        necessidades = Necessidade.objects.all().exclude(ind_excluido = True).filter(cod_necessidade_orgao = necessidade_orgao.cod_necessidade_orgao)
        total_necessidade = necessidades.filter(aprovado=False).count
        # Quem não é admin vê apenas os pedidos registrados em nome do órgão para o qual está autorizado
        return render(request, 'necessidade.html', {'estado': necessidade_orgao.estado,'necessidades' : necessidades, 'total_necessidade': total_necessidade, 'necessidade_orgao': necessidade_orgao, 'subordinados': subordinados_status, 'superior': superior, 'pode_registrar_demandas': pode_registrar_demandas, 'error': request.GET.get('error')})
    else:
        return redirect('error')

@login_required
@gestor_required
def necessidade_show(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    usuario = User.objects.get(id = request.user.id)
    orgao = Orgao.objects.get(nome = Profile.objects.get(user=usuario).orgao_ativo)
    gestor_orgao = True
    if orgao != necessidade.cod_necessidade_orgao.cod_orgao:
        gestor_orgao = False
    if request.method == 'GET':
        if gestor_orgao:
            return render(request, 'necessidade_show.html', {'necessidade' : necessidade})
        else:
            return render(request, 'error.html')
    elif request.method == 'POST' and gestor_orgao:
        necessidade = Necessidade.objects.get(cod_necessidade = pk)
        if request.POST['aprovado'] == 'True':
            necessidade.aprovado = True
        else:
            necessidade.aprovado = False
        necessidade.save()
        return redirect('/necessidade/' + pk + '/show')

@login_required
@gestor_required
def necessidade_new(request):
    if (hasattr(request.user, 'profile')):
        usuario = User.objects.get(id = request.user.id)
        orgao = Orgao.objects.get(nome = Profile.objects.get(user=usuario).orgao_ativo)
        try:
            plano_habilitado = Plano_Capacitacao.objects.filter(plano_habilitado = True)[0]
        except:
            return redirect('error')

        necessidade_orgao = Necessidade_Orgao.objects.all().get(cod_plano_capacitacao = plano_habilitado.cod_plano_capacitacao, cod_orgao = orgao.cod_orgao)
        txt_descricao = ''
        if(necessidade_orgao.estado==False):
            if request.method == "POST":
                txt_descricao = request.POST['txt_descricao']
                data = request.POST.copy()
                form = NecessidadeForm(request.POST)
                if form.is_valid():
                    necessidade = form.save(commit=False)
                    if request.POST['treinamento'] == '-1' and request.POST['txt_descricao']:
                        necessidade.txt_descricao = request.POST['txt_descricao']
                    elif request.POST['treinamento'] == '-1':
                        return render(request, 'necessidade_edit.html', {'form': form, 'erro_sugestao': "Preencha o campo de sugestão!", 'necessidade': necessidade})
                    else:
                        necessidade.txt_descricao = None
                        necessidade.cod_treinamento = Treinamento.objects.get(pk=request.POST['treinamento'])

                    if 'treinamento_externo' in request.POST and request.POST['valor_estimado']:
                        necessidade.txt_descricao = request.POST['txt_descricao']
                        necessidade.valor_estimado = request.POST['valor_estimado']
                    elif 'treinamento_externo' in request.POST:
                        return render(request, 'necessidade_edit.html', {'form': form, 'erro_valor_estimado': "Preencha o campo de valor estimado!", 'necessidade': necessidade})

                    necessidade.cod_usuario = usuario
                    necessidade.cod_necessidade_orgao = necessidade_orgao
                    necessidade.cod_orgao_origem = orgao
                    necessidade.save()
                    return redirect('necessidade')
                else:
                    return render(request, 'necessidade_edit.html', {'form': form, 'txt_descricao': txt_descricao})
            else:
                form = NecessidadeForm()
                return render(request, 'necessidade_edit.html', {'form': form, 'txt_descricao': txt_descricao})
        else:
            return redirect('error')
    else:
        return redirect('error')

@login_required
@gestor_required
def necessidade_edit(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    usuario = User.objects.get(id = request.user.id)
    orgao = Orgao.objects.get(nome = Profile.objects.get(user=usuario).orgao_ativo)
    planos_habilitados = Plano_Capacitacao.objects.filter(plano_habilitado = True)
    necessidade_updated = {
        'treinamento': necessidade.cod_treinamento.cod_treinamento,
        'cod_nivel': necessidade.cod_nivel.cod_nivel,
        'cod_area_conhecimento': necessidade.cod_area_conhecimento.cod_area_conhecimento,
        'cod_modalidade': necessidade.cod_modalidade.cod_modalidade,
        'hor_duracao': necessidade.hor_duracao,
        'cod_tipo_treinamento': necessidade.cod_tipo_treinamento.cod_tipo_treinamento,
        'cod_prioridade': necessidade.cod_prioridade.cod_prioridade,
        'qtd_servidor': necessidade.qtd_servidor,
        'cod_objetivo_treinamento': necessidade.cod_objetivo_treinamento.cod_objetivo_treinamento,
        'justificativa': necessidade.justificativa,
        'txt_descricao': necessidade.txt_descricao,
        'ementa': necessidade.ementa,
        'treinamento_externo': necessidade.treinamento_externo,
        'valor_estimado': necessidade.valor_estimado,
    }

    gestor_orgao = True #Começa considerando que é o usuário é do mesmo orgão que a necessidade
    if orgao != necessidade.cod_necessidade_orgao.cod_orgao:
        gestor_orgao = False

    if gestor_orgao:
        if request.method == "POST":
            necessidade_updated['txt_descricao'] = request.POST['txt_descricao']
            necessidade_updated['valor_estimado'] = request.POST['valor_estimado']
            form = NecessidadeForm(request.POST, instance=necessidade)
            if form.is_valid():
                necessidade = form.save(commit=False)
                if request.POST['treinamento'] == '-1' and request.POST['txt_descricao']:
                    necessidade.cod_treinamento = Treinamento.objects.get(pk=request.POST['treinamento'])
                    necessidade.txt_descricao = request.POST['txt_descricao']
                elif request.POST['treinamento'] == '-1':
                    return render(request, 'necessidade_edit.html', {'form': form, 'erro_sugestao': "Preencha o campo de sugestão!", 'necessidade': necessidade})
                else:
                    necessidade.txt_descricao = ""
                    necessidade.cod_treinamento = Treinamento.objects.get(pk=request.POST['treinamento'])
                if 'treinamento_externo' in request.POST and request.POST['valor_estimado']:
                    necessidade.valor_estimado = float(request.POST['valor_estimado'])
                elif 'treinamento_externo' in request.POST:
                    return render(request, 'necessidade_edit.html', {'form': form, 'erro_valor_estimado': "Preencha o campo de valor estimado!", 'necessidade': necessidade})

                necessidade.cod_usuario = usuario
                necessidade_orgao = Necessidade_Orgao.objects.all().get(cod_plano_capacitacao = planos_habilitados[0].cod_plano_capacitacao, cod_orgao = orgao.cod_orgao)
                necessidade.cod_necessidade_orgao = necessidade_orgao
                necessidade.save()
                return redirect('necessidade')
            else:
                return render(request, 'necessidade_edit.html', {'form': form, 'necessidade': necessidade_updated})

        else:
            form = NecessidadeForm(necessidade_updated, instance=necessidade)
            return render(request, 'necessidade_edit.html', {'form': form, 'necessidade': necessidade_updated})
    else:
        return render(request, 'error.html')

@login_required
@gestor_required
def necessidade_delete(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    usuario = User.objects.get(id = request.user.id)
    orgao = Orgao.objects.get(nome = Profile.objects.get(user=usuario).orgao_ativo)

    gestor_orgao = True
    if orgao != necessidade.cod_orgao_origem:
        gestor_orgao = False

    if necessidade.cod_necessidade_orgao.importado == False and gestor_orgao:
        necessidade.ind_excluido = 1
        necessidade.save()
        return redirect("necessidade")
    else:
        return render(request, 'error.html')

@gestor_required
def necessidade_approve(request, pk):
    Necessidade.objects.exclude(cod_necessidade_orgao__importado = True).filter(pk=pk).update(aprovado=False)
    return redirect("necessidade")

@gestor_required
def necessidade_disapprove(request, pk):
    Necessidade.objects.exclude(cod_necessidade_orgao__importado = True).filter(pk=pk).update(aprovado=True)
    return redirect("necessidade")

@gestor_required
def necessidade_orgao_close(request, pk):
    Necessidade_Orgao.objects.filter(pk=pk).update(estado=True)
    return redirect("necessidade")

@gestor_required
def cancelar_envio(request, pk):
    necessidade = Necessidade_Orgao.objects.filter(pk=pk)[0]
    if necessidade.importado == False:
        necessidade.estado = False
        necessidade.save()
        return redirect("necessidade")
    else:
        error(request, 'O pedido já foi importado')
        return redirect("necessidade")

@gestor_required
def importar_necessidade(request, pk, pk_atual):
    necessidade_orgao = get_object_or_404(Necessidade_Orgao, pk=pk)
    if necessidade_orgao.estado == True:
        necessidade_orgao.importado = True
        necessidade_orgao.save()
        necessidades = Necessidade.objects.all().filter(cod_necessidade_orgao = necessidade_orgao.cod_necessidade_orgao, aprovado=True)
        for necessidade in necessidades:
            necessidade_importada = necessidade
            necessidade_importada.aprovado = True
            necessidade_importada.cod_necessidade = None
            necessidade_importada.cod_necessidade_orgao = Necessidade_Orgao.objects.get(cod_necessidade_orgao = pk_atual)
            necessidade_importada.save()
        return redirect("necessidade")
    else:
        error(request, 'O pedido deste orgão foi cancelado')
        return redirect('necessidade')
        # return redirect(reverse('necessidade')+"?error=O pedido deste orgão foi cancelado")

@gestor_required
def devolver_necessidade(request, pk, pk_atual):
    necessidade_orgao = get_object_or_404(Necessidade_Orgao, pk=pk)
    orgao = necessidade_orgao.cod_orgao
    necessidade_orgao.importado = False
    necessidade_orgao.estado = False
    necessidade_orgao.save()
    necessidades = Necessidade.objects.all().filter(cod_orgao_origem_id = orgao, cod_necessidade_orgao_id = pk_atual)
    for necessidade in necessidades:
        necessidade.delete()
    return redirect("necessidade")

@admin_required
def orgaos_superiores(request):
        orgaos = Orgao.objects.all().filter(cod_superior=None)
        orgaos_superiores = []
        plano = Plano_Capacitacao.objects.filter(plano_habilitado=True)[0]
        for orgao in orgaos:
            necessidade_orgao = Necessidade_Orgao.objects.all().filter(cod_orgao=orgao, cod_plano_capacitacao=plano)[0]
            orgaos_superiores.append({"nome": orgao.nome,"estado": necessidade_orgao.estado})
        orgaos_superiores = sorted(orgaos_superiores, key=lambda x: x['estado'], reverse=True)
        return render(request, 'orgaos_superiores.html', {'orgaos_superiores': orgaos_superiores})

