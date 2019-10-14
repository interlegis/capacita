from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from capacita.decorators import admin_required
from .models import *
from .forms import *
from capacita.template_context_processors import is_admin

@login_required
@admin_required
def tipos_treinamento(request):
    tipos = Tipo_Treinamento.objects.all()
    return render(request, 'tipo_treinamento.html', {'tipos' : tipos})

@login_required
@admin_required
def tipo_treinamento_delete(request, pk):
    try:
        Tipo_Treinamento.objects.filter(pk=pk).delete()
        return redirect("tipos_treinamento")
    except Exception as e:
        print(e)
        tipos = Tipo_Treinamento.objects.all()
        return render(request, 'deleteError.html', {'url': 'tipo_treinamento.html', 'tipos': tipos})

@login_required
@admin_required
def tipo_treinamento_invisible(request, pk):
    Tipo_Treinamento.objects.filter(pk=pk).update(ind_excluido=True)
    return redirect("tipos_treinamento")

@login_required
@admin_required
def tipo_treinamento_visible(request, pk):
    Tipo_Treinamento.objects.filter(pk=pk).update(ind_excluido=False)
    return redirect("tipos_treinamento")

@login_required
@admin_required
def tipo_treinamento_edit(request,id):
    tipo = get_object_or_404(Tipo_Treinamento, pk=id)
    if request.method == 'POST':
        form = TipoTreinamentoForm(request.POST, instance=tipo, initial={'ind_excluido' : 0})
        if form.is_valid():
            form.save()
            return redirect("tipos_treinamento")
        else:
            return render(request, 'tipo_treinamento_edit.html', {'form' : form})
    else:
        form = TipoTreinamentoForm(instance=tipo)
        return render(request, 'tipo_treinamento_edit.html', {'form' : form})

@login_required
@admin_required
def tipo_treinamento_new(request):
    if request.method == 'POST':
        form = TipoTreinamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tipos_treinamento")
        else:
            return render(request, 'tipo_treinamento_edit.html', {'form' : form})
    else:
        form = TipoTreinamentoForm()
        return render(request, 'tipo_treinamento_edit.html', {'form' : form})
