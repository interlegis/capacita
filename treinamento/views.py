from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from capacita.template_context_processors import is_admin


@login_required
def treinamentos(request):
    treinamentos = Treinamento.objects.all().exclude(pk=-1)
    admin = is_admin(request)
    if admin:
        return render(request, 'treinamento.html', {'treinamentos' : treinamentos})
    else:
        return render(request, 'error.html')

@login_required
def treinamento_edit(request, pk):
    treinamento = get_object_or_404(Treinamento, pk=pk)
    admin = is_admin(request)
    if admin and request.method == "POST":
        form = TreinamentoForm(request.POST, instance=treinamento)
        if form.is_valid():
            treinamento = form.save(commit=False)
            treinamento.save()
            return redirect('treinamentos')
    elif request.method != "POST" and admin:
        form = TreinamentoForm(instance=treinamento)
    else:
        return render(request, 'error.html')
    return render(request, 'treinamento_edit.html', {'form': form})

@login_required
def treinamento_new(request):
    admin = is_admin(request)
    if admin and request.method == "POST":
        form = TreinamentoForm(request.POST)
        if form.is_valid():
            treinamento = form.save(commit=False)
            treinamento.save()
            return redirect('treinamentos')
    elif request.method != "POST" and admin:
        form = TreinamentoForm()
    else:
        return render(request, 'error.html')
    return render(request, 'treinamento_edit.html', {'form': form})

@login_required
def treinamento_delete(request, pk):
    admin = is_admin(request)
    if admin:
        treinamento = get_object_or_404(Treinamento, pk=pk)
        treinamento.ind_excluido = True
        treinamento.save()
        return redirect("treinamentos")
    else:
        return render(request, 'error.html')

@login_required
def treinamento_undelete(request, pk):
    admin = is_admin(request)
    if admin:
        treinamento = get_object_or_404(Treinamento, pk=pk)
        treinamento.ind_excluido = False
        treinamento.save()
        return redirect("treinamentos")
    else:
        return render(request, 'error.html')
