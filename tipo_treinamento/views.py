from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from capacita.template_context_processors import is_admin

@login_required
def tipos_treinamento(request):
    admin = is_admin(request)
    tipos = Tipo_Treinamento.objects.all()
    if admin:
        return render(request, 'tipo_treinamento.html', {'tipos' : tipos})
    else:
        return render(request, 'error.html')

@login_required
def tipo_treinamento_delete(request, pk):
    admin = is_admin(request)
    if admin:
        tipo = get_object_or_404(Tipo_Treinamento, pk=pk)
        tipo.ind_excluido = 1
        tipo.save()
        return redirect("tipos_treinamento")
    else:
        return render(request, 'error.html')

@login_required
def tipo_treinamento_undelete(request, pk):
    admin = is_admin(request)
    if admin:
        tipo = get_object_or_404(Tipo_Treinamento, pk=pk)
        tipo.ind_excluido = 0
        tipo.save()
        return redirect("tipos_treinamento")
    else:
        return render(request, 'error.html')

@login_required
def tipo_treinamento_edit(request,id):
    tipo = get_object_or_404(Tipo_Treinamento, pk=id)
    admin = is_admin(request)
    if request.method == 'POST' and admin:
        form = TipoTreinamentoForm(request.POST, instance=tipo, initial={'ind_excluido' : 0})
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect("tipos_treinamento")
    elif request.method != 'POST':
        form = TipoTreinamentoForm(instance=tipo)
    else:
        return render(request, 'error.html')
    return render(request, 'tipo_treinamento_edit.html', {'form' : form})

@login_required
def tipo_treinamento_new(request):
    admin = is_admin(request)
    if request.method == 'POST':
        form = TipoTreinamentoForm(request.POST)
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect("tipos_treinamento")
    elif request.method != 'POST':
        form = TipoTreinamentoForm()
    else:
        return render(request, 'error.html')
    return render(request, 'tipo_treinamento_edit.html', {'form' : form})
