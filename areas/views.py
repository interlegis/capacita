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
