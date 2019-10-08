# Decorator
from django.shortcuts import render

from capacita.template_context_processors import is_admin


def admin_required(func):
    def wrapper(request):
        if not is_admin(request)['is_admin']:
            return render(request, 'error.html')
        return func(request)
    return wrapper