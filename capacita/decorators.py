# Decorator
from django.shortcuts import render

from capacita.template_context_processors import is_admin, is_gestor


def admin_required(func):
    def wrapper(request, **kwargs):
        if not is_admin(request)['is_admin']:
            return render(request, 'error.html')
        return func(request, **kwargs)
    return wrapper

def gestor_required(func):
    def wrapper(request, **kwargs):
        if not is_gestor(request):
            return render(request, 'error.html')
        return func(request, **kwargs)
    return wrapper
