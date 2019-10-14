from django import forms
from django.contrib.auth.models import User, Group
from capacitaApp.models import *



class UserForm(forms.ModelForm):

    username = forms.CharField(max_length=100)
    first_name = ""
    last_name = ""
    is_staff = False
    is_active = True
    is_superuser = False


    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['style'] = 'text-transform:lowercase;'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active')
        # labels = {
        #     'username' : 'Login'
        # }
