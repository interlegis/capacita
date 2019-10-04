from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from capacita.decorators import admin_required
from .forms import *


@login_required
@admin_required
def treinamentos(request):
    treinamentos = Treinamento.objects.all().exclude(pk=-1)
    return render(request, 'treinamento.html', {'treinamentos' : treinamentos})

@login_required
@admin_required
def treinamento_edit(request, pk):
    treinamento = get_object_or_404(Treinamento, pk=pk)
    if request.method == "POST":
        form = TreinamentoForm(request.POST, instance=treinamento)
        if form.is_valid():
            form.save()
            return redirect('treinamentos')
        else:
            return render(request, 'treinamento_edit.html', {'form': form})
    else:
        form = TreinamentoForm(instance=treinamento)
        return render(request, 'treinamento_edit.html', {'form': form})

@login_required
@admin_required
def treinamento_new(request):
    if request.method == "POST":
        form = TreinamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('treinamentos')
        else:
            return render(request, 'treinamento_edit.html', {'form': form})
    elif request.method != "POST":
        form = TreinamentoForm()
        return render(request, 'treinamento_edit.html', {'form': form})

@login_required
@admin_required
def treinamento_invisible(request, pk):
    Treinamento.objects.filter(pk=pk).update(ind_excluido=True)
    return redirect("treinamentos")

@login_required
@admin_required
def treinamento_visible(request, pk):
    Treinamento.objects.filter(pk=pk).update(ind_excluido=False)
    return redirect("treinamentos")

@login_required
def treinamento_delete(request, pk):
    treinamentos = Treinamento.objects.all().exclude(pk=-1)
    try:
        Treinamento.objects.filter(pk=pk).delete()
        return redirect("treinamentos")
    except Exception as e:
        print(e)
        return render(request, 'deleteError.html', {'url': 'treinamento.html', 'treinamentos': treinamentos})

