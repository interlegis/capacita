from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from capacita.template_context_processors import is_admin


@login_required
def treinamentos(request):
    treinamentos = Treinamento.objects.all().exclude(pk=-1)
    if is_admin(request)['is_admin']:
        return render(request, 'treinamento.html', {'treinamentos' : treinamentos})
    else:
        return render(request, 'error.html')

@login_required
def treinamento_edit(request, pk):
    treinamento = get_object_or_404(Treinamento, pk=pk)
    admin = is_admin(request)['is_admin']
    if request.method == "POST" and admin:
        form = TreinamentoForm(request.POST, instance=treinamento)
        if form.is_valid():
            treinamento = form.save()
            return redirect('treinamentos')
        else:
            return render(request, 'treinamento_edit.html', {'form': form})
    elif request.method != "POST" and admin:
        form = TreinamentoForm(instance=treinamento)
        return render(request, 'treinamento_edit.html', {'form': form})
    else:
        return render(request, 'error.html')

@login_required
def treinamento_new(request):
    admin = is_admin(request)['is_admin']
    if request.method == "POST" and admin:
        form = TreinamentoForm(request.POST)
        if form.is_valid():
            treinamento = form.save()
            return redirect('treinamentos')
        else:
            return render(request, 'treinamento_edit.html', {'form': form})
    elif request.method != "POST" and admin:
        form = TreinamentoForm()
        return render(request, 'treinamento_edit.html', {'form': form})
    else:
        return render(request, 'error.html')

@login_required
def treinamento_invisible(request, pk):
    if is_admin(request)['is_admin']:
        Treinamento.objects.filter(pk=pk).update(ind_excluido=True)
        return redirect("treinamentos")
    else:
        return render(request, 'error.html')

@login_required
def treinamento_visible(request, pk):
    if is_admin(request)['is_admin']:
        Treinamento.objects.filter(pk=pk).update(ind_excluido=False)
        return redirect("treinamentos")
    else:
        return render(request, 'error.html')

@login_required
def treinamento_delete(request, pk):
    if is_admin(request)['is_admin']:
        try:
            Treinamento.objects.filter(pk=pk).delete()
            return redirect("treinamentos")
        except Exception as e:
            print(e)
            return render(request, 'deleteError.html', {'url': 'treinamentos.html'})
    else:
        return render(request, 'error.html')
