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

@login_required
def home(request):
  return render(request, 'capacita/home.html')


@login_required
def plano(request):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
    else:
        permissao = False
    planos = Plano_Capacitacao.objects.all()
    group = Group.objects.get(name='admin')
    group2 = Group.objects.get(name='gestor')
    form = PlanoForm()

    if (group in request.user.groups.all() or group2 in request.user.groups.all()):
        return render(request, 'capacita/plano_capacitacao.html', {'planos' : planos, 'form' : form, 'permissao' : permissao})
    else:
        return render(request, 'capacita/error.html')

@login_required
def plano_delete(request, id):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        plano = get_object_or_404(Plano_Capacitacao, pk=id)
        plano.delete()
        return redirect("plano")

@login_required
def plano_show(request, id):
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    return render(request, 'capacita/plano_show.html', {'plano' : plano})

@login_required
def plano_new(request):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
    else:
        permissao = False
    if request.method == "POST":
        form = PlanoForm(request.POST)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.save()
            return redirect('plano')
    else:
        form = PlanoForm()
    if(permissao):
        return render(request, 'capacita/plano_edit.html', {'form': form})
    else:
        return redirect('error')

@login_required
def plano_edit(request, id):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
    else:
        permissao = False
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    if request.method == "POST":
        form = PlanoForm(request.POST, instance=plano)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.save()
            return redirect("plano")
    else:
        form = PlanoForm(instance=plano)
    if(permissao):

        return render(request, 'capacita/plano_edit.html', {'form' : form})
    else:
        return redirect('error')

@login_required
def necessidade(request):
    if (hasattr(request.user, 'profile')):
        areas = Area_Conhecimento.objects.all()
        niveis = Nivel.objects.all()
        planos = Plano_Capacitacao.objects.all()
        groupAdmin = Group.objects.get(name='admin')
        groupGestor = Group.objects.get(name='gestor')
        groupSolicitante = Group.objects.get(name='solicitante')

        profile_usuario = Profile.objects.get(user_id = request.user.id)
        orgao_usuario = Orgao.objects.get(cod_orgao=profile_usuario.orgao_id)

        if(groupAdmin in request.user.groups.all()):
            is_admin = True
        else:
            is_admin = False

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

        # FIXME retornar filtro assim que ele for simplificado
        #necessidades = necessidade_query(area,nivel,plano,turno, int(qtd_servidor))
        #necessidades = necessidades.filter(ind_excluido = 0)
        necessidades = Necessidade.objects.all()

        # Quem não é admin vê apenas os pedidos registrados em nome do órgão para o qual está autorizado
        if(is_admin == False):
            necessidades = necessidades.filter(cod_orgao__orgao_id = request.user.profile.orgao_id)

        if(groupAdmin in request.user.groups.all() or 
            groupGestor in request.user.groups.all() or 
            groupSolicitante in request.user.groups.all() or 
            request.user.profile.permissao_necessidade == True):
            return render(request, 'capacita/necessidade.html', 
                {'necessidades' : necessidades, 'areas' : areas, 'niveis' : niveis, 'planos' : planos, 
                 'orgao_usuario' : orgao_usuario, 'is_admin' : is_admin})
        else:
            return render(request, 'capacita/error.html')
    else:
        return redirect('error')

@login_required
def necessidade_show(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    group = Group.objects.get(name='admin')
    group2 = Group.objects.get(name='gestor')

    if request.method == 'GET':
        if group in request.user.groups.all():
            is_admin = True
        else:
            is_admin = False

        if ((group in request.user.groups.all() or group2 in request.user.groups.all()) or request.user.profile.permissao_necessidade == True):
            return render(request, 'capacita/necessidade_show.html', {'necessidade' : necessidade, 'is_admin' : is_admin})
        else:
            return redirect("/error")
    else:
        if request.method == 'POST':
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
        areas = Area_Conhecimento.objects.all()
        treinamentos = Treinamento.objects.all()
        usuario = User.objects.get(id = request.user.id)
        group = Group.objects.get(name='gestor')
        group2 = Group.objects.get(name='admin')
        
        #FIXME mover esse teste para antes da criação de curso
        planos_habilitados = Plano_Capacitacao.objects.filter(plano_habilitado = True)

        if(planos_habilitados.count() > 0):
            if request.method == "POST":
                data = request.POST.copy()
                form = NecessidadeForm(request.POST)
                if form.is_valid():
                    necessidade = form.save(commit=False)
                    necessidade.cod_plano_capacitacao = planos_habilitados[0]
                    if (request.POST.get('curso_id', None)):
                        necessidade.treinamento = Treinamento.objects.get(cod_treinamento = request.POST.get('curso_id', None))
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

                if (group in request.user.groups.all() or group2 in request.user.groups.all() or usuario.profile.permissao_necessidade == True ):
                    return render(request, 'capacita/necessidade_edit.html', {'form': form, 'areas' : areas, 'eh_necessidade' : False, 'planos_habilitados' : planos_habilitados, 'treinamentos' : treinamentos})
                else:
                    return render(request, 'capacita/necessidade_edit.html', {'form': form})
        else:
            return render(request, 'capacita/necessidade_edit.html', {'form': form})
    else:
        #return render(request, 'capacita/necessidade_edit.html', {'form': form})
        return redirect('error')


@login_required
def necessidade_edit(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    treinamentos = Treinamento.objects.all()
    usuario = User.objects.get(id = request.user.id)
    group = Group.objects.get(name='gestor')
    group2 = Group.objects.get(name='admin')
    areas = Area_Conhecimento.objects.all()

    planos_habilitados = Plano_Capacitacao.objects.filter(plano_habilitado = True);

    if (group in request.user.groups.all() or group2 in request.user.groups.all()):
        if request.method == "POST":
            form = NecessidadeForm(request.POST, instance=necessidade)
            if form.is_valid():
                necessidade = form.save(commit=False)
                necessidade.cod_plano_capacitacao = Plano_Capacitacao.objects.get(cod_plano_capacitacao = request.POST['plano'])
                if (request.POST.get('curso_id', None)):
                    necessidade.treinamento = Treinamento.objects.get(cod_treinamento = request.POST.get('curso_id', None))
                necessidade.txt_descricao = request.POST.get('txt_descricao', None)
                necessidade.save()
                return redirect('necessidade')
        else:
            form = NecessidadeForm(instance=necessidade)
        return render(request, 'capacita/necessidade_edit.html', {'form': form, 'areas' : areas, 'planos_habilitados' : planos_habilitados, 'necessidade' : necessidade, 'treinamentos' : treinamentos})
    else:
        return render(request, 'capacita/error.html')

@login_required
def necessidade_delete(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    necessidade.ind_excluido = 1
    necessidade.save()
    return redirect("necessidade")

@login_required
def orgao(request):
    if (hasattr(request.user, 'profile')):
        orgaos_list = Orgao.objects.all()
        page = request.GET.get('page', 1)
        group = Group.objects.get(name='admin')
        group2 = Group.objects.get(name='gestor')
        paginator = Paginator(orgaos_list, 10)
        permissao = False

        if(group in request.user.groups.all()):
            permissao = True

        paginator = Paginator(orgaos_list, 6)
        try:
            orgaos = paginator.page(page)
        except PageNotAnInteger:
            orgaos = paginator.page(1)
        except EmptyPage:
            orgaos = paginator.page(paginator.num_pages)

        return render(request, 'capacita/orgao.html', {'orgaos' : orgaos, 'permissao' : permissao})
    else:
        return redirect('error')

@login_required
def orgao_edit(request, pk):
    orgao = get_object_or_404(Orgao, pk=pk)
    if request.method == "POST":
        form = OrgaoForm(request.POST, instance=orgao)
        if form.is_valid():
            orgao = form.save(commit=False)
            orgao.save()
            return redirect('orgao')
    else:
        form = OrgaoForm(instance=orgao)
    return render(request, 'capacita/orgao_edit.html', {'form': form})

@login_required
def orgao_new(request):
    if request.method == "POST":
        form = OrgaoForm(request.POST)
        if form.is_valid():
            orgao = form.save(commit=False)
            orgao.save()
            return redirect('orgao')
    else:
        form = OrgaoForm()
    return render(request, 'capacita/orgao_edit.html', {'form': form})

@login_required
def orgao_delete(request, id):
    orgao = get_object_or_404(Orgao, pk=id)
    orgao.delete()
    return redirect("orgao")

@login_required
def tipo(request):
    if (hasattr(request.user, 'profile')):
        group = Group.objects.get(name='admin')
        if (group in request.user.groups.all()):
            permissao = True
        else:
            permissao = False
        tipos = Tipo_Plano_Capacitacao.objects.filter(ind_excluido = 0)
        return render(request, 'capacita/tipo_plano.html', {'tipos' : tipos, 'permissao' : permissao})
    else:
        return redirect('error')

@login_required
def tipo_delete(request, pk):
    tipo = get_object_or_404(Tipo_Plano_Capacitacao, pk=pk)
    tipo.ind_excluido = 1
    tipo.save()
    return redirect("tipo")

@login_required
def tipo_edit(request,id):
    tipo = get_object_or_404(Tipo_Plano_Capacitacao, pk=id)
    if request.method == 'POST':
        form = TipoForm(request.POST, instance=tipo, initial={'ind_excluido' : 0})
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect("tipo")
    else:
        form = TipoForm(instance=tipo)
    return render(request, 'capacita/tipo_edit.html', {'form' : form})

@login_required
def tipo_new(request):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
    else:
        permissao = False
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect("tipo")
    else:
        form = TipoForm()

    if (permissao == True):
        return render(request, 'capacita/tipo_edit.html', {'form' : form, 'permissao' : permissao})
    else:
        return redirect('error')

@login_required
def relatorio(request):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Necessidades.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.set_column(0, 9, 20)
    worksheet.set_column(4, 4, 40)

    bold = workbook.add_format({'bold': True, 'center_across' : True})
    center = workbook.add_format({'center_across' : True})


    necessidades = Necessidade.objects.all()
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

        if (necessidade.cod_treinamento == '' or necessidade.cod_treinamento == None):
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
        worksheet.write(row, col + 8, '', center) #FIXME recuperar tipo de treinamento
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

@login_required
def areas(request):
    if (hasattr(request.user, 'profile')):
        area_filtrada = request.GET.get('cod_area_conhecimento_id', '')
        group = Group.objects.get(name='admin')
        if (group in request.user.groups.all()):
            permissao = True
        else:
            permissao = False
        return render(request, 'capacita/areas.html', { 'area_filtrada' : area_filtrada, 'permissao' : permissao})
    else:
        return redirect('error')

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

        group = Group.objects.get(name='gestor')
        group2 = Group.objects.get(name='admin')

    else:
        profiles = Profile.objects.all()
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

        return render(request, 'capacita/usuarios.html', {'users' : users, 'profiles' : profiles, 'orgao' : orgao, 'orgaos' : orgaos})
    else:
        if ((group in request.user.groups.all())):
            return render(request, 'capacita/usuarios.html', {'users' : users, 'profiles' : profiles, 'orgao' : orgao})
        else:
            return render(request, 'capacita/error.html')

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
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
    else:
        permissao = False

    if request.method == 'POST':
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
                return render(request, 'capacita/usuario_edit.html', {'form' : form, 'orgaos' : orgaos, 'groups' : groups, 'usuario' : True})

            return redirect("usuarios")
        else:
            print("Error: ", form.errors)
            return render(request, 'capacita/usuario_edit.html', {'form' : form})
    else:
        form = UserForm()
        orgaos = Orgao.objects.all()
        groups = Group.objects.all()

    orgaos = Orgao.objects.all()
    groups = Group.objects.all()

    if(permissao):
        return render(request, 'capacita/usuario_edit.html', {'form' : form, 'orgaos' : orgaos, 'groups' : groups, 'usuario' : True})
    else:
        return redirect('error')

@login_required
def usuario_edit(request, pk):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
    else:
        permissao = False
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
    if(permissao == True):
        return render(request, 'capacita/usuario_edit.html', {'form': form, 'orgaos' : orgaos, 'groups' : groups, 'usuario' : usuario})
    else:
        return redirect('error')

@login_required
def modalidade(request):
    if (hasattr(request.user, 'profile')):
        group = Group.objects.get(name = 'admin')
        permissao = False
        if group in request.user.groups.all():
            permissao = True

        modalidades = Modalidade_Treinamento.objects.filter(ind_excluido = False)
        return render(request, 'capacita/modalidades.html', {'modalidades' : modalidades, 'permissao' : permissao})
    else:
        return redirect('error')

@login_required
def eventos(request):
    if (hasattr(request.user, 'profile')):
        group = Group.objects.get(name = 'admin')
        permissao = False
        if group in request.user.groups.all():
            permissao = True

        eventos = Evento.objects.filter(ind_excluido = False)
        return render(request, 'capacita/eventos.html', {'eventos' : eventos, 'permissao' : permissao})
    else:
        return redirect('error')

@login_required
def evento_edit(request, pk):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
    else:
        permissao = False
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.save()
            return redirect('eventos')
    else:
        form = EventoForm(instance=evento)

    if(permissao == True):
        return render(request, 'capacita/evento_edit.html', {'form': form})
    else:
        return redirect('error')

@login_required
def evento_new(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.save()
            return redirect('eventos')
    else:
        form = EventoForm()
    return render(request, 'capacita/evento_edit.html', {'form': form})

@login_required
def evento_delete(request, pk):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
        evento = get_object_or_404(Evento, pk=pk)
        evento.ind_excluido = True
        evento.save()
        return redirect("eventos")
    else:
        return redirect('error')

@login_required
def modalidade_edit(request, pk):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
    else:
        permissao = False
    modalidade = get_object_or_404(Modalidade_Treinamento, pk=pk)
    if request.method == "POST":
        form = ModalidadeForm(request.POST, instance=modalidade)
        if form.is_valid():
            modalidade = form.save(commit=False)
            modalidade.save()
            return redirect('modalidade')
    else:
        form = ModalidadeForm(instance=modalidade)

    if(permissao == True):
        return render(request, 'capacita/modalidade_edit.html', {'form': form})
    else:
        return redirect('error')

@login_required
def modalidade_new(request):
    if request.method == "POST":
        form = ModalidadeForm(request.POST)
        if form.is_valid():
            modalidade = form.save(commit=False)
            modalidade.save()
            return redirect('modalidade')
    else:
        form = ModalidadeForm()
    return render(request, 'capacita/modalidade_edit.html', {'form': form})

@login_required
def modalidade_delete(request, pk):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
        modalidade = get_object_or_404(Modalidade_Treinamento, pk=pk)
        modalidade.ind_excluido = True
        modalidade.save()
        return redirect("modalidade")
    else:
        return redirect('error')

@login_required
def api_areas(request):
    areas = Area_Conhecimento.objects.all().values()

    areas = list(areas)

    return JsonResponse(areas, safe=False)

@login_required
def api_cursos(request):
    treinamentos = Treinamento.objects.all().values()
    treinamentos = list(treinamentos)
    return JsonResponse(treinamentos, safe=False)

@login_required
def api_tipos(request):
    tipos = Tipo_Plano_Capacitacao.objects.all().values()
    tipos = list(tipos)
    return JsonResponse(tipos, safe=False)

@login_required
def api_planos(request):
    planos = Plano_Capacitacao.objects.all().values()
    planos = list(planos)
    return JsonResponse(planos, safe=False)

@login_required
def error(request):
    return render(request, 'capacita/error.html')

@login_required
def avaliacao_cursos(request):
    # group = Group.objects.get(name='admin')
    # if (group in request.user.groups.all()):
    if request.method == "POST":
        necessidade = Necessidade.objects.get(cod_necessidade = request.POST['cod_necessidade'])
        necessidade.txt_descricao = None
        treinamento = Treinamento.objects.create(nome = request.POST['txt'], cod_area_conhecimento = necessidade.cod_area_conhecimento)
        treinamento.save()
        necessidade.treinamento = treinamento
        necessidade.save()

        return redirect('avaliacao_cursos')
    else:
        cursos_necessidades = Necessidade.objects.exclude(txt_descricao = None).exclude(txt_descricao = '')
        return render(request, "capacita/avaliacao_cursos.html", {'necessidades' : cursos_necessidades})
    # else:
    #     return redirect('error')
