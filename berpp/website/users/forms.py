from django import forms
from django.contrib.auth.models import User
#from users.models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
