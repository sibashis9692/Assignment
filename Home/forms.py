from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegistrationForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',  'id': 'username'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control',  'id': 'email'}),
    )
    password = forms.CharField(
        label='Password',  
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password1'}),
    )
    password_confirmation = forms.CharField(
        label='Confirm_Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'id': 'confirmPassword'}),
    )



class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'id': 'typePasswordX'}),
    )
    

    def clean(self):

        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')


        if not username:
            raise forms.ValidationError('Username is required.')

        if not password:
            raise forms.ValidationError('Password is required.')

        return cleaned_data
