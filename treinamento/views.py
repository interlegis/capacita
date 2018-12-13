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
def treinamentos(request):
    treinamentos = Treinamento.objects.all().exclude(pk=-1)
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        return render(request, 'capacita/treinamento.html', {'treinamentos' : treinamentos, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def treinamento_edit(request, pk):
    treinamento = get_object_or_404(Treinamento, pk=pk)
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin and request.method == "POST":
        form = TreinamentoForm(request.POST, instance=treinamento)
        if form.is_valid():
            treinamento = form.save(commit=False)
            treinamento.save()
            return redirect('treinamentos')
    elif request.method != "POST" and admin:
        form = TreinamentoForm(instance=treinamento)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/treinamento_edit.html', {'form': form, 'is_admin':admin, 'is_gestor': gestor})

@login_required
def treinamento_new(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin and request.method == "POST":
        form = TreinamentoForm(request.POST)
        if form.is_valid():
            treinamento = form.save(commit=False)
            treinamento.save()
            return redirect('treinamentos')
    elif request.method != "POST" and admin:
        form = TreinamentoForm()
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'capacita/treinamento_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})

@login_required
def treinamento_delete(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        treinamento = get_object_or_404(Treinamento, pk=pk)
        treinamento.ind_excluido = True
        treinamento.save()
        return redirect("treinamentos")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def treinamento_undelete(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        treinamento = get_object_or_404(Treinamento, pk=pk)
        treinamento.ind_excluido = False
        treinamento.save()
        return redirect("treinamentos")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
