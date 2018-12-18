from capacitaApp.models import *
from django.contrib.auth.models import User

def include_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Exception as e:
        profile = []
    return {'profile': profile}

def is_admin(request):
    if AuthUserGroups.objects.filter(user_id = request.user.id).filter(group_id = 1).exists():
        return {'is_admin': True}
    else:
        return {'is_admin': False}

def is_gestor(request):
    if AuthUserGroups.objects.filter(user_id = request.user.id).filter(group_id = 2).exists():
        return {'is_gestor': True}
    else:
        return {'is_gestor': False}
