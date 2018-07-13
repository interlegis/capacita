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

def necessidade_new(request):
    if request.method == "POST":
        form = NecessidadeForm(request.POST)
        if form.is_valid():
            necessidade = form.save(commit=False) 
            necessidade.save()
            return redirect('home')
    else:
        form = NecessidadeForm()
    return render(request, 'novo_capacita/necessidade_edit.html', {'form': form})

def plano_new(request):
    if request.method == "POST":
        form = PlanoForm(request.POST)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.save()
            return redirect('home')
    else:
        form = PlanoForm()
    return render(request, 'novo_capacita/plano_edit.html', {'form' : form})

def necessidade_edit(request, pk):
    necessidade = get_object_or_404(Necessidade, pk=pk)
    if request.method == "POST":
        form = NecessidadeForm(request.POST, instance=necessidade)
        if form.is_valid():
            necessidade = form.save(commit=False)
            necessidade.save()
            return redirect('home')
    else:
        form = AcaoForm(instance=acao)
    return render(request, 'novo_capacita/necessidade_edit.html', {'form': form})

