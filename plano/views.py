from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from capacita.template_context_processors import is_admin

@login_required
def plano(request):
    planos = Plano_Capacitacao.objects.all()
    form = PlanoForm()
    admin = is_admin(request)

    if admin:
        return render(request, 'plano_capacitacao.html', {'planos' : planos, 'form' : form})
    else:
        return render(request, 'error.html')

@login_required
def plano_delete(request, id):
    admin = is_admin(request)
    if (admin):
        plano = get_object_or_404(Plano_Capacitacao, pk=id)
        plano.ind_excluido = 1
        plano.save()
        return redirect("plano")
    else:
        return render(request, 'error.html')

@login_required
def plano_undelete(request, id):
    admin = is_admin(request)
    if (admin):
        plano = get_object_or_404(Plano_Capacitacao, pk=id)
        plano.ind_excluido = 0
        plano.save()
        return redirect("plano")
    else:
        return render(request, 'error.html')


@login_required
def plano_show(request, id):
    admin = is_admin(request)
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    if admin:
        return render(request, 'plano_show.html', {'plano' : plano})
    else:
        return redirect('error')

@login_required
def plano_new(request):
    admin = is_admin(request)
    if request.method == "POST":
        form = PlanoForm(request.POST)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.save()
            for orgao in Orgao.objects.all():
                Necessidade_Orgao.objects.create(cod_orgao = orgao, cod_plano_capacitacao = plano, estado = False)

            return redirect('plano')
    else:
        form = PlanoForm()
    if(admin):
        return render(request, 'plano_edit.html', {'form': form})
    else:
        return redirect('error')

@login_required
def plano_edit(request, id):
    admin = is_admin(request)
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    if request.method == "POST":
        form = PlanoForm(request.POST, instance=plano)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.save()
            return redirect("plano")
    else:
        form = PlanoForm(instance=plano)
    if(admin):
        return render(request, 'plano_edit.html', {'form' : form})
    else:
        return redirect('error')
