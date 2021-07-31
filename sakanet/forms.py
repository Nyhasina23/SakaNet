from django import forms
from .models import Utilisateur

class UserRegister(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom_user','password','email','nom','prenom']        
