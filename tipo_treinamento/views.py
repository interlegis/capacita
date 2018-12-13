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
def tipos_treinamento(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    tipos = Tipo_Treinamento.objects.all()
    if admin:
        return render(request, 'tipo_treinamento.html', {'tipos' : tipos, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})

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
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})

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
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})

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
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'tipo_treinamento_edit.html', {'form' : form, 'is_admin': admin, 'is_gestor': gestor})

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
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'tipo_treinamento_edit.html', {'form' : form, 'is_admin': admin, 'is_gestor': gestor})
