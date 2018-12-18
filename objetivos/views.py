from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from capacitaApp.views import is_admin

@login_required
def objetivos(request):
    admin = is_admin(request)
    if admin:
        objetivos = Objetivo_Treinamento.objects.all()
        return render(request, 'objetivos.html', {'objetivos' : objetivos})
    else:
        return render(request, 'error.html')

@login_required
def objetivo_edit(request, pk):
    admin = is_admin(request)
    objetivo = get_object_or_404(Objetivo_Treinamento, pk=pk)
    if request.method == "POST" and admin:
        form = ObjetivoTreinamentoForm(request.POST, instance=objetivo)
        if form.is_valid():
            objetivo = form.save(commit=False)
            objetivo.save()
            return redirect('objetivos')
    elif request.method != "POST" and admin:
        form = ObjetivoTreinamentoForm(instance=objetivo)
    else:
        return render(request, 'error.html')
    return render(request, 'objetivo_edit.html', {'form': form})

@login_required
def objetivo_new(request):
    admin = is_admin(request)
    if request.method == "POST" and admin:
        form = ObjetivoTreinamentoForm(request.POST)
        if form.is_valid():
            objetivo = form.save(commit=False)
            objetivo.save()
            return redirect('objetivos')
    elif request.method != "POST" and admin:
        form = ObjetivoTreinamentoForm()
    else:
        return render(request, 'error.html')
    return render(request, 'objetivo_edit.html', {'form': form})

@login_required
def objetivo_delete(request, pk):
    admin = is_admin(request)
    if admin:
        objetivo = get_object_or_404(Objetivo_Treinamento, pk=pk)
        objetivo.ind_excluido = 1
        objetivo.save()
        return redirect("objetivos")
    else:
        return render(request, 'error.html')

@login_required
def objetivo_undelete(request, pk):
    admin = is_admin(request)
    if admin:
        objetivo = get_object_or_404(Objetivo_Treinamento, pk=pk)
        objetivo.ind_excluido = 0
        objetivo.save()
        return redirect("objetivos")
    else:
        return render(request, 'error.html')
