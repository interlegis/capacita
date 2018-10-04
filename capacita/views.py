# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
import xlsxwriter
from .filtro_necessidade import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from .filters import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

def home(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    else:
        return render(request, 'capacita/home.html')

def plano(request):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
    else:
        permissao = False
    planos = Plano_Capacitacao.objects.all()
    plano_filter = PlanoFilter(request.GET, queryset=planos)
    group = Group.objects.get(name='admin')
    group2 = Group.objects.get(name='gestor')
    form = PlanoForm()

    if (group in request.user.groups.all() or group2 in request.user.groups.all()):
        return render(request, 'capacita/plano_capacitacao.html', {'filter' : plano_filter, 'form' : form, 'permissao' : permissao})
    else:
        return render(request, 'capacita/error.html')

def plano_delete(request, id):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        plano = get_object_or_404(Plano_Capacitacao, pk=id)
        plano.delete()
        return redirect("plano")
    

def plano_show(request, id):
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    return render(request, 'capacita/plano_show.html', {'plano' : plano})
    

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

def necessidade(request):
    if (hasattr(request.user, 'profile')):
        areas = Area_Conhecimento.objects.all()
        niveis = Nivel.objects.all()
        turnos = Turno.objects.all()
        planos = Plano_Capacitacao.objects.all()
        group = Group.objects.get(name='admin')
        group2 = Group.objects.get(name='gestor')
        group3 = Group.objects.get(name='solicitante')
        
        profile_usuario = Profile.objects.get(user_id = request.user.id)
        orgao_usuario = Orgao.objects.get(cod_orgao=profile_usuario.orgao_id)

        if(group in request.user.groups.all()):
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
        if  request.GET.get('plano'):
            plano = request.GET.get('plano')
        if  request.GET.get('turno'):
            turno = request.GET.get('turno')
        if  request.GET.get('qtd_servidor'):
            qtd_servidor = request.GET.get('qtd_servidor')

        necessidades = necessidade_query(area,nivel,plano,turno, int(qtd_servidor))
        necessidades = necessidades.order_by('custo')

        if(group in request.user.groups.all() or group2 in request.user.groups.all() or group3 in request.user.groups.all() or request.user.profile.permissao_necessidade == True):
            return render(request, 'capacita/necessidade.html', {'necessidades' : necessidades, 'areas' : areas, 'niveis' : niveis, 'planos' : planos, 'turnos' : turnos, 'orgao_usuario' : orgao_usuario, 'is_admin' : is_admin})
        else:
            return render(request, 'capacita/error.html')
    else:
        return redirect('error')

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
            

def necessidade_new(request):
    if (hasattr(request.user, 'profile')):
        areas = Area_Conhecimento.objects.all()
        cursos = Curso.objects.all()
        usuario = User.objects.get(id = request.user.id)
        group = Group.objects.get(name='gestor')
        group2 = Group.objects.get(name='admin')
        form2 = SubAreaForm()

        planos_habilitados = Plano_Capacitacao.objects.filter(plano_habilitado = True);

        if(planos_habilitados.count() > 0):
            if request.method == "POST":
                data = request.POST.copy()
                form = NecessidadeForm(request.POST)
                if form.is_valid():
                    necessidade = form.save(commit=False) 
                    necessidade.cod_plano_capacitacao = Plano_Capacitacao.objects.get(cod_plano_capacitacao = request.POST['plano'])
                    if (request.POST.get('curso_id', None)):
                        necessidade.curso = Curso.objects.get(cod_curso = request.POST.get('curso_id', None))
                    necessidade.txt_descricao = request.POST.get('txt_descricao', None)
                    necessidade.save()
                    return redirect('necessidade')
                else:
                    return redirect("/error")
            else:
                form = NecessidadeForm()
            
                if (group in request.user.groups.all() or group2 in request.user.groups.all() or usuario.profile.permissao_necessidade == True ):
                    return render(request, 'capacita/necessidade_edit.html', {'form': form, 'areas' : areas, 'form2' : form2, 'eh_necessidade' : False, 'planos_habilitados' : planos_habilitados, 'cursos' : cursos})
                else: 
                    return render(request, 'capacita/error.html')
        else:
            return render(request, 'capacita/error.html', {'eh_necessidade' : True})
    else:
        return redirect('error')

def necessidade_edit(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    cursos = Curso.objects.all()
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
                    necessidade.curso = Curso.objects.get(cod_curso = request.POST.get('curso_id', None))
                necessidade.txt_descricao = request.POST.get('txt_descricao', None)
                necessidade.save()
                return redirect('necessidade')
        else:
            form = NecessidadeForm(instance=necessidade)
        return render(request, 'capacita/necessidade_edit.html', {'form': form, 'areas' : areas, 'planos_habilitados' : planos_habilitados, 'necessidade' : necessidade, 'cursos' : cursos})
    else:
        return render(request, 'capacita/error.html')

def necessidade_delete(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    necessidade.delete()
    return redirect("necessidade")

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

def orgao_delete(request, id):
    orgao = get_object_or_404(Orgao, pk=id)
    orgao.delete()
    return redirect("orgao")

def tipo(request):
    if (hasattr(request.user, 'profile')):
        group = Group.objects.get(name='admin')
        if (group in request.user.groups.all()):
            permissao = True
        else:
            permissao = False
        tipos = Tipo_Plano_Capacitacao.objects.all()
        return render(request, 'capacita/tipo_plano.html', {'tipos' : tipos, 'permissao' : permissao})
    else:
        return redirect('error')

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

def relatorio(request):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Necessidades.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.set_column(0, 9, 20)
    worksheet.set_column(4, 4, 40)
        
    bold = workbook.add_format({'bold': True, 'center_across' : True})
    center = workbook.add_format({'center_across' : True})

    necessidades = Necessidade.objects.all()

    row = 0
    col = 0

    worksheet.write(row, col,         "Descricao", bold)
    worksheet.write(row, col + 1,     "Plano", bold)
    worksheet.write(row, col + 2,     "Iniciativa", bold)
    worksheet.write(row, col + 3,     "Prioridade", bold)
    worksheet.write(row, col + 4,     "Quantidade de Servidores", bold)
    worksheet.write(row, col + 5,     "Area Conhecimento", bold)
    worksheet.write(row, col + 6,     "Nivel", bold)
    worksheet.write(row, col + 7,     "Hora de Duração", bold)
    worksheet.write(row, col + 8,     "Turno", bold)
    worksheet.write(row, col + 9,     "Mês", bold)

    row += 1

    for necessidade in necessidades:
        worksheet.write(row, col,     necessidade.txt_descricao, center)
        worksheet.write(row, col + 1, necessidade.cod_plano_capacitacao.situacao, center)
        worksheet.write(row, col + 2, necessidade.cod_iniciativa.nome, center)
        worksheet.write(row, col + 3, necessidade.cod_prioridade.nome, center)
        worksheet.write(row, col + 4, necessidade.qtd_servidor, center)
        worksheet.write(row, col + 5, necessidade.cod_sub_area_conhecimento.txt_descricao, center)
        worksheet.write(row, col + 6, necessidade.cod_nivel.nome, center)
        worksheet.write(row, col + 7, necessidade.hor_duracao, center)
        worksheet.write(row, col + 8, necessidade.cod_turno.nome, center)
        worksheet.write(row, col + 9, necessidade.cod_mes.nome, center)
        row += 1

    worksheet.set_default_row(20)

    workbook.close()

    fh = open("Necessidades.xlsx", 'rb')

    response = HttpResponse(fh) # mimetype is replaced by content_type for django 1.7
    response['Content-Disposition'] = 'attachment; filename=%s' % "Necessidades.xlsx"
    response['X-Sendfile'] = fh

    return response

def areas(request):
    if (hasattr(request.user, 'profile')):
        area_filtrada = request.GET.get('cod_area_conhecimento_id', '')
        group = Group.objects.get(name='admin')
        if (group in request.user.groups.all()):
            permissao = True
        else:
            permissao = False
        
        if area_filtrada != '':
            sub_areas = Sub_Area_Conhecimento.objects.filter(cod_area_conhecimento_id = area_filtrada)
        else:
            sub_areas = Sub_Area_Conhecimento.objects.all()  

        subarea_filter = SubAreaFilter(request.GET, queryset=sub_areas)

        form = SubAreaForm()
        page = request.GET.get('page', 1)

        paginator = Paginator(sub_areas, 10)
        try:
            subs = paginator.page(page)
        except PageNotAnInteger:
            subs = paginator.page(1)
        except EmptyPage:
            subs = paginator.page(paginator.num_pages)

        return render(request, 'capacita/areas.html', { 'subs': subs, 'filter' : subarea_filter, 'area_filtrada' : area_filtrada, 'permissao' : permissao})
    else:
        return redirect('error')
        
def sub_area_edit(request, pk):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
    else:
        permissao = False
    sub_area = get_object_or_404(Sub_Area_Conhecimento, pk=pk)
    if request.method == "POST":
        form = SubAreaForm(request.POST, instance=sub_area)
        if form.is_valid():
            sub_area = form.save(commit=False)
            sub_area.save()
            return redirect('areas')
    else:
        form = SubAreaForm(instance=sub_area)
    
    if(permissao == True):
        return render(request, 'capacita/area_edit.html', {'form': form})
    else:
        return redirect('error')

def subarea_delete(request, id):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        subarea = get_object_or_404(Sub_Area_Conhecimento, pk=id)
        subarea.delete()
        return redirect("areas")
    else:
        return redirect('error') 

def subareas_new(request):
    group = Group.objects.get(name='admin')
    if (group in request.user.groups.all()):
        permissao = True
    else:
        permissao = False
    if request.method == 'POST':
        form = SubAreaForm(request.POST)
        if form.is_valid():
            subarea = form.save(commit=False)
            subarea.save()
            return redirect("areas")
    else:
        form = SubAreaForm()
    if(permissao == True):
        return render(request, 'capacita/area_edit.html', {'form' : form})
    else:
        return redirect('error')

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
            usuario = form.save()
            profile = Profile.objects.create(titular = False, permissao_necessidade = False, orgao_id = request.POST['orgao'], user_id = usuario.id)
            usuario.is_active = True
            usuario.groups.add(my_group)
            profile.save()
            usuario.save()
            
            return redirect("usuarios")
        else:
            return redirect('error')
    else:
        form = UserForm()
        orgaos = Orgao.objects.all()
        groups = Group.objects.all()

        if(permissao):
            return render(request, 'capacita/usuario_edit.html', {'form' : form, 'orgaos' : orgaos, 'groups' : groups})
        else:
            return redirect('error')

def api_areas(request):
    areas = Area_Conhecimento.objects.all().values()
    sub_areas = Sub_Area_Conhecimento.objects.all()

    areas = list(areas)

    return JsonResponse(areas, safe=False)

def api_subareas(request):
    subareas = Sub_Area_Conhecimento.objects.all().values()
    subareas = list(subareas)
    return JsonResponse(subareas, safe=False)

def api_cursos(request):
    cursos = Curso.objects.all().values()
    cursos = list(cursos)
    return JsonResponse(cursos, safe=False)

def error(request):
    return render(request, 'capacita/error.html')
