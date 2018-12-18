from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
from capacitaApp.views import is_admin, is_gestor
from areas.models import *
from treinamento.models import *
from plano.models import *
from tipo_treinamento.models import *

@login_required
def api_areas(request):
    admin_or_gestor = is_admin(request) or is_gestor(request)
    if(admin_or_gestor):
        areas = Area_Conhecimento.objects.all().exclude(ind_excluido = True).values()
        areas = list(areas)
    else:
        return render(request, 'error.html')
    return JsonResponse(areas, safe=False)

@login_required
def api_cursos(request):
    admin_or_gestor = is_admin(request) or is_gestor(request)
    if(admin_or_gestor):
        treinamentos = Treinamento.objects.all().exclude(ind_excluido = True).values()
        treinamentos = list(treinamentos)
    else:
        return render(request, 'error.html')
    return JsonResponse(treinamentos, safe=False)

@login_required
def api_tipos_treinamento(request):
    admin_or_gestor = is_admin(request) or is_gestor(request)
    if(admin_or_gestor):
        tipos = Tipo_Treinamento.objects.all().exclude(ind_excluido = True).values()
        tipos = list(tipos)
    else:
        return render(request, 'error.html')
    return JsonResponse(tipos, safe=False)

@login_required
def api_planos(request):
    admin_or_gestor = is_admin(request) or is_gestor(request)
    if(admin_or_gestor):
        planos = Plano_Capacitacao.objects.all().exclude(ind_excluido = True).values()
        planos = list(planos)
    else:
        return render(request, 'error.html')
    return JsonResponse(planos, safe=False)
