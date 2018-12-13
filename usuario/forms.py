from django import forms
from django.contrib.auth.models import User, Group
from capacitaApp.models import *



class UserForm(forms.ModelForm):

    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    is_staff = False
    is_active = True
    is_superuser = False

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active')
        # labels = {
        #     'username' : 'Login'
        # }
