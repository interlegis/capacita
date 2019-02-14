from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from capacita.template_context_processors import is_admin

@login_required
def tipos_treinamento(request):
    tipos = Tipo_Treinamento.objects.all()
    if is_admin(request)['is_admin']:
        return render(request, 'tipo_treinamento.html', {'tipos' : tipos})
    else:
        return render(request, 'error.html')

@login_required
def tipo_treinamento_delete(request, pk):
    if is_admin(request)['is_admin']:
        try:
            Tipo_Treinamento.objects.filter(pk=pk).delete()
            return redirect("tipos_treinamento")
        except Exception as e:
            print(e)
            tipos = Tipo_Treinamento.objects.all()
            return render(request, 'deleteError.html', {'url': 'tipo_treinamento.html', 'tipos': tipos})
    else:
        return render(request, 'error.html')

@login_required
def tipo_treinamento_invisible(request, pk):
    if is_admin(request)['is_admin']:
        Tipo_Treinamento.objects.filter(pk=pk).update(ind_excluido=True)
        return redirect("tipos_treinamento")
    else:
        return render(request, 'error.html')

@login_required
def tipo_treinamento_visible(request, pk):
    if is_admin(request)['is_admin']:
        Tipo_Treinamento.objects.filter(pk=pk).update(ind_excluido=False)
        return redirect("tipos_treinamento")
    else:
        return render(request, 'error.html')

@login_required
def tipo_treinamento_edit(request,id):
    tipo = get_object_or_404(Tipo_Treinamento, pk=id)
    admin = is_admin(request)['is_admin']
    if request.method == 'POST' and admin:
        form = TipoTreinamentoForm(request.POST, instance=tipo, initial={'ind_excluido' : 0})
        if form.is_valid():
            tipo = form.save()
            return redirect("tipos_treinamento")
        else:
            return render(request, 'tipo_treinamento_edit.html', {'form' : form})
    elif request.method != 'POST' and admin:
        form = TipoTreinamentoForm(instance=tipo)
        return render(request, 'tipo_treinamento_edit.html', {'form' : form})
    else:
        return render(request, 'error.html')

@login_required
def tipo_treinamento_new(request):
    admin = is_admin(request)['is_admin']
    if request.method == 'POST' and admin:
        form = TipoTreinamentoForm(request.POST)
        if form.is_valid():
            tipo = form.save()
            return redirect("tipos_treinamento")
        else:
            return render(request, 'tipo_treinamento_edit.html', {'form' : form})
    elif request.method != 'POST' and admin:
        form = TipoTreinamentoForm()
        return render(request, 'tipo_treinamento_edit.html', {'form' : form})
    else:
        return render(request, 'error.html')
