from capacitaApp.models import *
from django.contrib.auth.models import User

def include_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Exception as e:
        profile = []
    return {'profile': profile}

def is_admin(request):
    try:
        admin = Profile.objects.get(user=request.user).is_admin
        return {'is_admin': admin}
    except Exception as e:
        return {'is_admin': False}


def is_gestor(request):
    try:
        profile = Profile.objects.get(user=request.user)
        orgaos = profile.orgaos
        if orgaos.filter(grupo_id = 2).filter(orgao = profile.orgao_ativo).exists():
            return {'is_gestor': True}
        else:
            return {'is_gestor': False}
    except Exception as e:
        return {'is_gestor': False}
