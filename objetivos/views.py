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
