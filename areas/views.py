from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from capacitaApp.views import is_admin, is_gestor

@login_required
def areas(request):
    if is_admin(request):
        areas = Area_Conhecimento.objects.all();
        return render(request, 'areas.html', { 'areas' : areas })
    else:
        return render(request, 'error.html')

@login_required
def area_delete(request, pk):
    if is_admin(request):
        Area_Conhecimento.objects.filter(pk=pk).update(ind_excluido=True)
        return redirect("areas")
    else:
        return render(request, 'error.html')

@login_required
def area_undelete(request, pk):
    if is_admin(request):
        Modalidade_Treinamento.objects.filter(pk=pk).update(ind_excluido=False)
        return redirect("areas")
    else:
        return render(request, 'error.html')

@login_required
def area_edit(request,id):
    admin = is_admin(request)
    area = get_object_or_404(Area_Conhecimento, pk=id)
    if request.method == 'POST' and admin:
        form = AreaConhecimentoForm(request.POST, instance=area, initial={'ind_excluido' : False})
        if form.is_valid():
            area = form.save()
            return redirect("areas")
        else:
            return render(request, 'area_edit.html', {'form' : form})
    elif request.method != 'POST' and admin:
        form = AreaConhecimentoForm(instance=area)
        return render(request, 'area_edit.html', {'form' : form})
    else:
        return render(request, 'error.html')

@login_required
def area_new(request):
    admin = is_admin(request)
    if request.method == 'POST' and admin:
        form = AreaConhecimentoForm(request.POST)
        if form.is_valid():
            area = form.save()
            return redirect("areas")
        else:
            return render(request, 'area_edit.html', {'form' : form})
    elif request.method != 'POST' and admin:
        form = AreaConhecimentoForm()
        return render(request, 'area_edit.html', {'form' : form})
    else:
        return render(request, 'error.html')
