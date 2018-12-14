from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from capacitaApp.views import is_gestor, is_admin

@login_required
def orgao(request):
    if (hasattr(request.user, 'profile')):
        orgaos_list = Orgao.objects.all()
        page = request.GET.get('page', 1)
        admin = is_admin(request)
        gestor = is_gestor(request)
        paginator = Paginator(orgaos_list, 10)
        permissao = False
        paginator = Paginator(orgaos_list, 6)
        if admin:
            try:
                orgaos = paginator.page(page)
            except PageNotAnInteger:
                orgaos = paginator.page(1)
            except EmptyPage:
                orgaos = paginator.page(paginator.num_pages)
            return render(request, 'orgao.html', {'orgaos' : orgaos, 'is_admin' : admin, 'is_gestor': gestor})
        else:
            return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})
    else:
        return redirect('error')

@login_required
def orgao_edit(request, pk):
    admin = is_admin(request)
    gestor = is_gestor(request)
    orgao = get_object_or_404(Orgao, pk=pk)
    if request.method == "POST" and admin:
        form = OrgaoForm(request.POST, instance=orgao)
        if form.is_valid():
            orgao = form.save(commit=False)
            orgao.save()
            return redirect('orgao')
    elif request.method != "POST" and admin:
        form = OrgaoForm(instance=orgao)
    else:
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'orgao_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})

@login_required
def orgao_new(request):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if request.method == "POST" and admin:
        form = OrgaoForm(request.POST)
        if form.is_valid():
            orgao = form.save(commit=False)
            orgao.save()
            return redirect('orgao')
    elif request.method != "POST" and admin:
        form = OrgaoForm()
    else:
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})
    return render(request, 'orgao_edit.html', {'form': form, 'is_admin': admin, 'is_gestor': gestor})

@login_required
def orgao_delete(request, id):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        orgao = Orgao.objects.filter(pk=id).update(ind_excluido=1)
        return redirect("orgao")
    else:
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})

@login_required
def orgao_undelete(request, id):
    admin = is_admin(request)
    gestor = is_gestor(request)
    if admin:
        orgao = Orgao.objects.filter(pk=id).update(ind_excluido=0)
        return redirect("orgao")
    else:
        return render(request, 'error.html', {'is_admin': admin, 'is_gestor': gestor})
