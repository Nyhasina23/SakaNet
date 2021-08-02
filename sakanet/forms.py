from django import forms
from .models import Utilisateur
from .models import User
from django.contrib.auth.forms import UserCreationForm 

class UserRegister(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']       
    
    def save(self , commit=True):
        user = super(UserRegister, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]