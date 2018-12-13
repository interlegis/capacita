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
def plano(request):
    planos = Plano_Capacitacao.objects.all()
    form = PlanoForm()
    admin = is_admin(request)
    gestor = is_gestor(request)

    if admin:
        return render(request, 'capacita/plano_capacitacao.html', {'planos' : planos, 'form' : form, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def plano_delete(request, id):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if (admin):
        plano = get_object_or_404(Plano_Capacitacao, pk=id)
        plano.ind_excluido = 1
        plano.save()
        return redirect("plano")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def plano_undelete(request, id):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if (admin):
        plano = get_object_or_404(Plano_Capacitacao, pk=id)
        plano.ind_excluido = 0
        plano.save()
        return redirect("plano")
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})


@login_required
def plano_show(request, id):
    admin = is_admin(request)
    gestor = is_gestor(request)
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    if admin:
        return render(request, 'capacita/plano_show.html', {'plano' : plano})
    else:
        return redirect('error')

@login_required
def plano_new(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if request.method == "POST":
        form = PlanoForm(request.POST)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.save()
            for orgao in Orgao.objects.all():
                Necessidade_Orgao.objects.create(cod_orgao = orgao, cod_plano_capacitacao = plano, estado = False)

            return redirect('plano')
    else:
        form = PlanoForm()
    if(admin):
        return render(request, 'capacita/plano_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')

@login_required
def plano_edit(request, id):
    admin = is_admin(request)
    gestor = is_gestor(request)
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    if request.method == "POST":
        form = PlanoForm(request.POST, instance=plano)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.save()
            return redirect("plano")
    else:
        form = PlanoForm(instance=plano)
    if(admin):
        return render(request, 'capacita/plano_edit.html', {'form' : form, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')
