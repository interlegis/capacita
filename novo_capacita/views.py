from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from .filters import *

def home(request):
    necessidades = Necessidade.objects.all()
    return render(request, 'novo_capacita/home.html', {'necessidades' : necessidades})

def plano(request):
    planos = Plano_Capacitacao.objects.all()
    plano_filter = PlanoFilter(request.GET, queryset=planos)
    form = PlanoForm()
    return render(request, 'novo_capacita/plano_capacitacao.html', {'filter' : plano_filter, 'form' : form})

def plano_delete(request, id):
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    plano.delete()
    return redirect("plano")

def plano_show(request, id):
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    return render(request, 'novo_capacita/plano_show.html', {'plano' : plano})
    

def plano_new(request):
    if request.method == "POST":
        form = PlanoForm(request.POST)
        if form.is_valid():
            plano = form.save(commit=False) 
            plano.save()
            return redirect('plano')
    else:
        form = PlanoForm()
    return render(request, 'novo_capacita/plano_edit.html', {'form': form})

def plano_edit(request, id):
    plano = get_object_or_404(Plano_Capacitacao, pk=id)
    if request.method == "POST":
        form = PlanoForm(request.POST, instance=plano)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.save()
            return redirect("plano")
    else:
        form = PlanoForm(instance=plano)
    return render(request, 'novo_capacita/plano_edit.html', {'form' : form})

def necessidade(request):
    necessidades = Necessidade.objects.all()
    return render(request, 'novo_capacita/necessidade.html', {'necessidades' : necessidades})

def necessidade_show(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    return render(request, 'novo_capacita/necessidade_show.html', {'necessidade' : necessidade})

def necessidade_new(request):
    if request.method == "POST":
        form = NecessidadeForm(request.POST)
        if form.is_valid():
            necessidade = form.save(commit=False) 
            necessidade.save()
            return redirect('necessidade')
    else:
        form = NecessidadeForm()
    return render(request, 'novo_capacita/necessidade_edit.html', {'form': form})

def necessidade_edit(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    if request.method == "POST":
        form = NecessidadeForm(request.POST, instance=necessidade)
        if form.is_valid():
            necessidade = form.save(commit=False)
            necessidade.save()
            return redirect('necessidade')
    else:
        form = NecessidadeForm(instance=necessidade)
    return render(request, 'novo_capacita/necessidade_edit.html', {'form': form})

def necessidade_delete(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    necessidade.delete()
    return redirect("necessidade")

def orgao(request):
    orgaos = Orgao.objects.all()
    return render(request, 'novo_capacita/orgao.html', {'orgaos' : orgaos})

def orgao_edit(request, pk):
    orgao = get_object_or_404(Orgao, pk=pk)
    if request.method == "POST":
        form = OrgaoForm(request.POST, instance=orgao)
        if form.is_valid():
            orgao = form.save(commit=False)
            orgao.save()
            return redirect('orgao')
    else:
        form = OrgaoForm(instance=orgao)
    return render(request, 'novo_capacita/orgao_edit.html', {'form': form})

def orgao_new(request):
    if request.method == "POST":
        form = OrgaoForm(request.POST)
        if form.is_valid():
            orgao = form.save(commit=False) 
            orgao.save()
            return redirect('orgao')
    else:
        form = OrgaoForm()
    return render(request, 'novo_capacita/orgao_edit.html', {'form': form})

def orgao_delete(request, id):
    orgao = get_object_or_404(Orgao, pk=id)
    orgao.delete()
    return redirect("orgao")