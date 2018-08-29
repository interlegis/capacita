# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
import xlsxwriter
from .models import *
from .forms import *
from .filters import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render(request, 'capacita/home.html')

def plano(request):
    planos = Plano_Capacitacao.objects.all()
    plano_filter = PlanoFilter(request.GET, queryset=planos)
    form = PlanoForm()
    return render(request, 'capacita/plano_capacitacao.html', {'filter' : plano_filter, 'form' : form})

def plano_delete(request, id):
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    plano.delete()
    return redirect("plano")

def plano_show(request, id):
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    return render(request, 'capacita/plano_show.html', {'plano' : plano})
    

def plano_new(request):
    if request.method == "POST":
        form = PlanoForm(request.POST)
        if form.is_valid():
            plano = form.save(commit=False) 
            plano.save()
            return redirect('plano')
    else:
        form = PlanoForm()
    return render(request, 'capacita/plano_edit.html', {'form': form})

def plano_edit(request, id):
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    if request.method == "POST":
        form = PlanoForm(request.POST, instance=plano)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.save()
            return redirect("plano")
    else:
        form = PlanoForm(instance=plano)
    return render(request, 'capacita/plano_edit.html', {'form' : form})

def necessidade(request):
    necessidades = Necessidade.objects.all()
    return render(request, 'capacita/necessidade.html', {'necessidades' : necessidades})

def necessidade_show(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    return render(request, 'capacita/necessidade_show.html', {'necessidade' : necessidade})

def necessidade_new(request):
    areas = Area_Conhecimento.objects.all()
    form2 = SubAreaForm()
    if request.method == "POST":
        form = NecessidadeForm(request.POST)
        if form.is_valid():
            necessidade = form.save(commit=False) 
            necessidade.save()
            return redirect('necessidade')
    else:
        form = NecessidadeForm()
    return render(request, 'capacita/necessidade_edit.html', {'form': form, 'areas' : areas, 'form2' : form2})

def necessidade_edit(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    areas = Area_Conhecimento.objects.all()
    if request.method == "POST":
        form = NecessidadeForm(request.POST, instance=necessidade)
        if form.is_valid():
            necessidade = form.save(commit=False)
            necessidade.save()
            return redirect('necessidade')
    else:
        form = NecessidadeForm(instance=necessidade)
    return render(request, 'capacita/necessidade_edit.html', {'form': form, 'areas' : areas})

def necessidade_delete(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    necessidade.delete()
    return redirect("necessidade")

def orgao(request):
    orgaos = Orgao.objects.all()
    return render(request, 'capacita/orgao.html', {'orgaos' : orgaos})

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
    tipos = Tipo_Plano_Capacitacao.objects.all()
    return render(request, 'capacita/tipo_plano.html', {'tipos' : tipos})

def tipo_edit(request,id):
    tipo = get_object_or_404(Tipo_Plano_Capacitacao, pk=id)
    if request.method == 'POST':
        form = TipoForm(request.POST, instance=tipo)
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect("tipo")
    else:
        form = TipoForm(instance=tipo)
    return render(request, 'capacita/tipo_edit.html', {'form' : form})

def tipo_new(request):
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect("tipo")
    else:
        form = TipoForm()
    return render(request, 'capacita/tipo_edit.html', {'form' : form})

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
        worksheet.write(row, col + 5, necessidade.cod_area_conhecimento.txt_descricao, center)
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

    area_filtrada = request.GET.get('cod_area_conhecimento_id', '')
    
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

    return render(request, 'capacita/areas.html', { 'subs': subs, 'filter' : subarea_filter, 'area_filtrada' : area_filtrada})

def sub_area_edit(request, pk):
    sub_area = get_object_or_404(Sub_Area_Conhecimento, pk=pk)
    if request.method == "POST":
        form = SubAreaForm(request.POST, instance=sub_area)
        if form.is_valid():
            sub_area = form.save(commit=False)
            sub_area.save()
            return redirect('areas')
    else:
        form = SubAreaForm(instance=sub_area)
    return render(request, 'capacita/area_edit.html', {'form': form})

def subarea_delete(request, id):
    subarea = get_object_or_404(Sub_Area_Conhecimento, pk=id)
    subarea.delete()
    return redirect("areas")

def subareas_new(request):
    if request.method == 'POST':
        form = SubAreaForm(request.POST)
        if form.is_valid():
            subarea = form.save(commit=False)
            subarea.save()
            return redirect("areas")
    else:
        form = SubAreaForm()
    return render(request, 'capacita/area_edit.html', {'form' : form})

def api_areas(request):
    areas = Area_Conhecimento.objects.all().values()
    sub_areas = Sub_Area_Conhecimento.objects.all()

    areas = list(areas)

    return JsonResponse(areas, safe=False)

def api_subareas(request):

    subareas = Sub_Area_Conhecimento.objects.all().values()

    subareas = list(subareas)

    return JsonResponse(subareas, safe=False)

