from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from capacitaApp.views import is_admin, is_gestor
from capacita.decorators import admin_required

@login_required
@admin_required
def areas(request):
    areas = Area_Conhecimento.objects.all();
    return render(request, 'areas.html', { 'areas' : areas })

@login_required
@admin_required
def area_delete(request, pk):
    try:
        Area_Conhecimento.objects.filter(pk=pk).delete()
        areas = Area_Conhecimento.objects.all();
        return redirect("areas")
    except Exception as e:
        print(e)
        areas = Area_Conhecimento.objects.all();
        return render(request, 'deleteError.html', {'url': 'areas.html', 'areas': areas})

@login_required
@admin_required
def area_invisible(request, pk):
    Area_Conhecimento.objects.filter(pk=pk).update(ind_excluido=True)
    return redirect("areas")

@login_required
@admin_required
def area_visible(request, pk):
    Area_Conhecimento.objects.filter(pk=pk).update(ind_excluido=False)
    return redirect("areas")

@login_required
@admin_required
def area_edit(request,id):
    area = get_object_or_404(Area_Conhecimento, pk=id)
    if request.method == 'POST':
        form = AreaConhecimentoForm(request.POST, instance=area, initial={'ind_excluido' : False})
        if form.is_valid():
            area = form.save()
            return redirect("areas")
        else:
            return render(request, 'area_edit.html', {'form' : form})
    else:
        form = AreaConhecimentoForm(instance=area)
        return render(request, 'area_edit.html', {'form' : form})

@login_required
@admin_required
def area_new(request):
    if request.method == 'POST':
        form = AreaConhecimentoForm(request.POST)
        if form.is_valid():
            area = form.save()
            return redirect("areas")
        else:
            return render(request, 'area_edit.html', {'form' : form})
    else:
        form = AreaConhecimentoForm()
        return render(request, 'area_edit.html', {'form' : form})
