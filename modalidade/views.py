from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from capacita.template_context_processors import is_admin

@login_required
def modalidade(request):
    if (hasattr(request.user, 'profile') and is_admin(request)['is_admin']):
        modalidades = Modalidade_Treinamento.objects.all()
        return render(request, 'modalidades.html', {'modalidades' : modalidades})
    else:
        return redirect('error')

@login_required
def modalidade_edit(request, pk):
    admin = is_admin(request)['is_admin']
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
    admin = is_admin(request)['is_admin']
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
    if is_admin(request)['is_admin']:
        try:
            Modalidade_Treinamento.objects.filter(pk=pk).delete()
            return redirect("modalidade")
        except Exception as e:
            print(e)
            return render(request, 'deleteError.html')
    else:
        return redirect('error')


@login_required
def modalidade_invisible(request, pk):
    if is_admin(request)['is_admin']:
        Modalidade_Treinamento.objects.filter(pk=pk).update(ind_excluido=True)
        return redirect("modalidade")
    else:
        return redirect('error')

@login_required
def modalidade_visible(request, pk):
    if is_admin(request)['is_admin']:
        Modalidade_Treinamento.objects.filter(pk=pk).update(ind_excluido=False)
        return redirect("modalidade")
    else:
        return redirect('error')
