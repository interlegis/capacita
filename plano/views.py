from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from capacita.decorators import admin_required
from .forms import *
from necessidade.models import *
from capacita.template_context_processors import is_admin

@login_required
@admin_required
def plano(request):
    planos = Plano_Capacitacao.objects.all()
    form = PlanoForm()
    return render(request, 'plano_capacitacao.html', {'planos' : planos, 'form' : form})

@login_required
@admin_required
def plano_delete(request, id):
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    try:
        plano.delete()
        return redirect("plano")
    except Exception as e:
        print(e)
        planos = Plano_Capacitacao.objects.all()
        return render(request, 'deleteError.html', {'url': 'plano_capacitacao.html', 'planos': planos})

@login_required
@admin_required
def plano_invisible(request, id):
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    plano.ind_excluido = 1
    plano.save()
    return redirect("plano")

@login_required
@admin_required
def plano_visible(request, id):
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    plano.ind_excluido = 0
    plano.save()
    return redirect("plano")


@login_required
@admin_required
def plano_show(request, id):
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    return render(request, 'plano_show.html', {'plano' : plano})

@login_required
def plano_new(request):
    admin = is_admin(request)['is_admin']
    if request.method == "POST" and admin:
        form = PlanoForm(request.POST)
        if form.is_valid():
            plano = form.save()
            for orgao in Orgao.objects.all(): #Cria uma necessidade orgão em todos os órgãos
                Necessidade_Orgao.objects.create(cod_orgao = orgao, cod_plano_capacitacao = plano, estado = False)
            return redirect('plano')
        else:
            return render(request, 'plano_edit.html', {'form': form})
    elif admin:
        form = PlanoForm()
        return render(request, 'plano_edit.html', {'form': form})
    else:
        return redirect('error')

@login_required
def plano_edit(request, id):
    admin = is_admin(request)['is_admin']
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    if request.method == "POST" and admin:
        form = PlanoForm(request.POST, instance=plano)
        if form.is_valid():
            plano = form.save()
            if plano.plano_habilitado:
                Plano_Capacitacao.objects.filter(plano_habilitado=True).exclude(cod_plano_capacitacao=plano.cod_plano_capacitacao).update(plano_habilitado=False)
                # plano.plano_habilitado=True
                # plano.save()
            return redirect("plano")
    elif admin:
        form = PlanoForm(instance=plano)
        return render(request, 'plano_edit.html', {'form' : form})
    else:
        return redirect('error')
