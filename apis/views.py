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
    if is_admin(request)['is_admin'] or is_gestor(request):
        areas = Area_Conhecimento.objects.all().exclude(ind_excluido = True).values()
        areas = list(areas)
    else:
        return render(request, 'error.html')
    return JsonResponse(areas, safe=False)

@login_required
def api_cursos(request):
    if is_admin(request)['is_admin'] or is_gestor(request):
        treinamentos = Treinamento.objects.all().exclude(ind_excluido = True).values()
        treinamentos = list(treinamentos)
    else:
        return render(request, 'error.html')
    return JsonResponse(treinamentos, safe=False)

@login_required
def api_tipos_treinamento(request):
    if is_admin(request)['is_admin'] or is_gestor(request):
        tipos = Tipo_Treinamento.objects.all().exclude(ind_excluido = True).values()
        tipos = list(tipos)
    else:
        return render(request, 'error.html')
    return JsonResponse(tipos, safe=False)

@login_required
def api_planos(request):
    if is_admin(request)['is_admin'] or is_gestor(request):
        planos = Plano_Capacitacao.objects.all().exclude(ind_excluido = True).values()
        planos = list(planos)
    else:
        return render(request, 'error.html')
    return JsonResponse(planos, safe=False)
