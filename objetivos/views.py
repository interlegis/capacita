from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from capacita.decorators import admin_required
from .models import *
from .forms import *
from capacitaApp.views import is_admin

@login_required
@admin_required
def objetivos(request):
    objetivos = Objetivo_Treinamento.objects.all()
    return render(request, 'objetivos.html', {'objetivos' : objetivos})

@login_required
@admin_required
def objetivo_edit(request, pk):
    objetivo = get_object_or_404(Objetivo_Treinamento, pk=pk)
    if request.method == "POST":
        form = ObjetivoTreinamentoForm(request.POST, instance=objetivo)
        if form.is_valid():
            objetivo = form.save()
            return redirect('objetivos')
        else:
            return render(request, 'objetivo_edit.html', {'form': form})
    elif request.method != "POST":
        form = ObjetivoTreinamentoForm(instance=objetivo)
        return render(request, 'objetivo_edit.html', {'form': form})
    else:
        return render(request, 'error.html')

@login_required
@admin_required
def objetivo_new(request):
    if request.method == "POST":
        form = ObjetivoTreinamentoForm(request.POST)
        if form.is_valid():
            objetivo = form.save()
            return redirect('objetivos')
        else:
            return render(request, 'objetivo_edit.html', {'form': form})
    elif request.method != "POST":
        form = ObjetivoTreinamentoForm()
        return render(request, 'objetivo_edit.html', {'form': form})
    else:
        return render(request, 'error.html')

@login_required
@admin_required
def objetivo_delete(request, pk):
    try:
        Objetivo_Treinamento.objects.filter(pk=pk).delete()
        return redirect("objetivos")
    except Exception as e:
        print(e)
        objetivos = Objetivo_Treinamento.objects.all()
        return render(request, 'deleteError.html', {'url': 'objetivos.html', 'objetivos': objetivos})

@login_required
@admin_required
def objetivo_invisible(request, pk):
    Objetivo_Treinamento.objects.filter(pk=pk).update(ind_excluido=True)
    return redirect("objetivos")

@login_required
@admin_required
def objetivo_visible(request, pk):
    Objetivo_Treinamento.objects.filter(pk=pk).update(ind_excluido=False)
    return redirect("objetivos")
