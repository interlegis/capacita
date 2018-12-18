from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from capacita.template_context_processors import is_admin

@login_required
def modalidade(request):
    admin = is_admin(request)
    if (hasattr(request.user, 'profile')):
        modalidades = Modalidade_Treinamento.objects.all()
        return render(request, 'modalidades.html', {'modalidades' : modalidades, 'permissao' : admin})
    else:
        return redirect('error')

@login_required
def modalidade_edit(request, pk):
    admin = is_admin(request)
    modalidade = get_object_or_404(Modalidade_Treinamento, pk=pk)
    if request.method == "POST" and admin:
        form = ModalidadeForm(request.POST, instance=modalidade)
        if form.is_valid():
            modalidade = form.save(commit=False)
            modalidade.save()
            return redirect('modalidade')
    elif request.method != "POST" and admin:
        form = ModalidadeForm(instance=modalidade)
    else:
        return render(request, 'error.html')

    if(admin):
        return render(request, 'modalidade_edit.html', {'form': form})
    else:
        return redirect('error')

@login_required
def modalidade_new(request):
    admin = is_admin(request)
    if request.method == "POST" and admin:
        form = ModalidadeForm(request.POST)
        if form.is_valid():
            modalidade = form.save(commit=False)
            modalidade.save()
            return redirect('modalidade')
    elif request.method != "POST" and admin:
        form = ModalidadeForm()
    else:
        return render(request, 'error.html')
    return render(request, 'modalidade_edit.html', {'form': form})

@login_required
def modalidade_delete(request, pk):
    admin = is_admin(request)
    if (admin):
        modalidade = get_object_or_404(Modalidade_Treinamento, pk=pk)
        modalidade.ind_excluido = True
        modalidade.save()
        return redirect("modalidade")
    else:
        return redirect('error')

@login_required
def modalidade_undelete(request, pk):
    admin = is_admin(request)
    if (admin):
        modalidade = get_object_or_404(Modalidade_Treinamento, pk=pk)
        modalidade.ind_excluido = False
        modalidade.save()
        return redirect("modalidade")
    else:
        return redirect('error')
