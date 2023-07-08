from django import forms


from app.models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets={'password':forms.PasswordInput()}



class FreedomFightersForm(forms.ModelForm):
    class Meta():
        model = FreedomFighters
        fields = "__all__"