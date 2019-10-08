from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from capacita.decorators import admin_required
from .forms import *

@login_required
@admin_required
def sugestao(request):
    sugestoes = Sugestao.objects.all()
    return render(request, 'sugestao.html', {'sugestoes' : sugestoes})

@login_required
@admin_required
def sugestao_new(request):
    if request.method == "POST":
        form = SugestaoForm(request.POST)
        if form.is_valid():
            sugestao = form.save(commit=False)
            user = User.objects.get(id = request.user.id)
            sugestao.cod_usuario = user
            sugestao.save()
            return redirect('sugestao')
    else:
        form = SugestaoForm()
    return render(request, 'sugestao_edit.html', {'form': form})
