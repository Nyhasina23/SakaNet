from django import forms
from django.forms import (
    Form,
    ModelForm,
    ModelChoiceField,
    CharField,
)
# from .models import Utilisateur
from .models import User
from .models import Message
from .models import Publication
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

class MessagesForm(ModelForm):
    class Meta:
        model = Message
        fields = ["message"]

class PubForm(ModelForm):
    class Meta:
        model = Publication
        fields = ["contenus_pub"]