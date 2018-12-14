from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from capacitaApp.views import is_gestor, is_admin

@login_required
def modalidade(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if (hasattr(request.user, 'profile')):
        modalidades = Modalidade_Treinamento.objects.all()
        return render(request, 'modalidades.html', {'modalidades' : modalidades, 'permissao' : admin, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')

@login_required
def modalidade_edit(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
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
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})

    if(admin):
        return render(request, 'modalidade_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')

@login_required
def modalidade_new(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if request.method == "POST" and admin:
        form = ModalidadeForm(request.POST)
        if form.is_valid():
            modalidade = form.save(commit=False)
            modalidade.save()
            return redirect('modalidade')
    elif request.method != "POST" and admin:
        form = ModalidadeForm()
    else:
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'modalidade_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})

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