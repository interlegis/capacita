from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from capacitaApp.views import is_admin, is_gestor

@login_required
def areas(request):
    admin = is_admin(request)
    if admin:
        areas = Area_Conhecimento.objects.all();
        return render(request, 'areas.html', { 'areas' : areas })
    else:
        return render(request, 'error.html')

@login_required
def area_delete(request, pk):
    admin = is_admin(request)
    if admin:
        area = get_object_or_404(Area_Conhecimento, pk=pk)
        area.ind_excluido = 1
        area.save()
        return redirect("areas")
    else:
        return render(request, 'error.html')

@login_required
def area_undelete(request, pk):
    admin = is_admin(request)
    if admin:
        area = get_object_or_404(Area_Conhecimento, pk=pk)
        area.ind_excluido = 0
        area.save()
        return redirect("areas")
    else:
        return render(request, 'error.html')

@login_required
def area_edit(request,id):
    admin = is_admin(request)
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
        return render(request, 'error.html')
    return render(request, 'area_edit.html', {'form' : form})

@login_required
def area_new(request):
    admin = is_admin(request)
    if request.method == 'POST' and admin:
        form = AreaConhecimentoForm(request.POST)
        if form.is_valid():
            area = form.save(commit=False)
            area.save()
            return redirect("areas")
    elif request.method != 'POST':
        form = AreaConhecimentoForm()
    else:
        return render(request, 'error.html')
    return render(request, 'area_edit.html', {'form' : form})
