from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Avg, Max, Count, Sum
from django.contrib.auth.decorators import login_required

import xlsxwriter
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

from capacitaApp.views import *

@login_required
def api_areas(request):
    admin_or_gestor = is_admin(request) or is_gestor(request)
    if(admin_or_gestor):
        areas = Area_Conhecimento.objects.all().exclude(ind_excluido = True).values()
        areas = list(areas)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return JsonResponse(areas, safe=False)

@login_required
def api_cursos(request):
    admin_or_gestor = is_admin(request) or is_gestor(request)
    if(admin_or_gestor):
        treinamentos = Treinamento.objects.all().exclude(ind_excluido = True).values()
        treinamentos = list(treinamentos)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return JsonResponse(treinamentos, safe=False)

@login_required
def api_tipos_treinamento(request):
    admin_or_gestor = is_admin(request) or is_gestor(request)
    if(admin_or_gestor):
        tipos = Tipo_Treinamento.objects.all().exclude(ind_excluido = True).values()
        tipos = list(tipos)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return JsonResponse(tipos, safe=False)

@login_required
def api_planos(request):
    admin_or_gestor = is_admin(request) or is_gestor(request)
    if(admin_or_gestor):
        planos = Plano_Capacitacao.objects.all().exclude(ind_excluido = True).values()
        planos = list(planos)
    else:
        return render(request, 'capacita/error.html', {'is_admin': admin, 'is_gestor': gestor})
    return JsonResponse(planos, safe=False)
