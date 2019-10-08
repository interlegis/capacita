from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from capacita.decorators import admin_required
from .forms import *

@login_required
@admin_required
def modalidade(request):
    if hasattr(request.user, 'profile'):
        modalidades = Modalidade_Treinamento.objects.all()
        return render(request, 'modalidades.html', {'modalidades': modalidades})
    else:
        return redirect('error')

@login_required
@admin_required
def modalidade_edit(request, pk):
    modalidade = get_object_or_404(Modalidade_Treinamento, pk=pk)
    if request.method == "POST":
        form = ModalidadeForm(request.POST, instance=modalidade)
        if form.is_valid():
            form.save()
            return redirect('modalidade')
        else:
            return render(request, 'modalidade_edit.html', {'form': form})
    else:
        form = ModalidadeForm(instance=modalidade)
        return render(request, 'modalidade_edit.html', {'form': form})

@login_required
@admin_required
def modalidade_new(request):
    if request.method == "POST":
        form = ModalidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modalidade')
        else:
            return render(request, 'modalidade_edit.html', {'form': form})
    else:
        form = ModalidadeForm()
        return render(request, 'modalidade_edit.html', {'form': form})


@login_required
@admin_required
def modalidade_delete(request, pk):
    try:
        Modalidade_Treinamento.objects.filter(pk=pk).delete()
        return redirect("modalidade")
    except Exception as e:
        print(e)
        modalidades = Modalidade_Treinamento.objects.all()
        return render(request, 'deleteError.html', {'url': 'modalidades.html', 'modalidades': modalidades})

@login_required
@admin_required
def modalidade_invisible(request, pk):
    Modalidade_Treinamento.objects.filter(pk=pk).update(ind_excluido=True)
    return redirect("modalidade")

@login_required
@admin_required
def modalidade_visible(request, pk):
    Modalidade_Treinamento.objects.filter(pk=pk).update(ind_excluido=False)
    return redirect("modalidade")
