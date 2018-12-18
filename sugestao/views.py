from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
from capacita.template_context_processors import is_gestor, is_admin

@login_required
def sugestao(request):
    admin = is_admin(request)
    user = User.objects.get(id = request.user.id)
    sugestoes = Sugestao.objects.all()
    if admin:
        return render(request, 'sugestao.html', {'sugestoes' : sugestoes, 'user' : user})
    else:
        return render(request, 'error.html')

@login_required
def sugestao_new(request):
    admin = is_admin(request)
    user = User.objects.get(id = request.user.id)
    if request.method == "POST" and admin:
        form = SugestaoForm(request.POST)
        if form.is_valid():
            sugestao = form.save(commit=False)
            sugestao.cod_usuario = user
            sugestao.save()
            return redirect('sugestao')
    elif request.method != "POST" and admin:
        form = SugestaoForm()
    else:
        return render(request, 'error.html')
    return render(request, 'sugestao_edit.html', {'form': form})
