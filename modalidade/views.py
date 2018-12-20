from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from capacita.template_context_processors import is_admin

@login_required
def modalidade(request):
    if (hasattr(request.user, 'profile') and is_admin(request)):
        modalidades = Modalidade_Treinamento.objects.all()
        return render(request, 'modalidades.html', {'modalidades' : modalidades})
    else:
        return redirect('error')

@login_required
def modalidade_edit(request, pk):
    admin = is_admin(request)
    modalidade = get_object_or_404(Modalidade_Treinamento, pk=pk)
    if request.method == "POST" and admin:
        form = ModalidadeForm(request.POST, instance=modalidade)
        if form.is_valid():
            modalidade = form.save()
            return redirect('modalidade')
        else:
            return render(request, 'modalidade_edit.html', {'form': form})
    elif request.method != "POST" and admin:
        form = ModalidadeForm(instance=modalidade)
        return render(request, 'modalidade_edit.html', {'form': form})
    else:
        return render(request, 'error.html')

@login_required
def modalidade_new(request):
    admin = is_admin(request)
    if request.method == "POST" and admin:
        form = ModalidadeForm(request.POST)
        if form.is_valid():
            modalidade = form.save()
            return redirect('modalidade')
        else:
            return render(request, 'modalidade_edit.html', {'form': form})
    elif request.method != "POST" and admin:
        form = ModalidadeForm()
        return render(request, 'modalidade_edit.html', {'form': form})
    else:
        return render(request, 'error.html')

@login_required
def modalidade_delete(request, pk):
    if is_admin(request):
        Modalidade_Treinamento.objects.filter(pk=pk).update(ind_excluido=True)
        return redirect("modalidade")
    else:
        return redirect('error')

@login_required
def modalidade_undelete(request, pk):
    if is_admin(request):
        Modalidade_Treinamento.objects.filter(pk=pk).update(ind_excluido=False)
        return redirect("modalidade")
    else:
        return redirect('error')
