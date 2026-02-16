from django import forms
from books import models
from django.contrib.auth.models import User

class BookCreateForm(forms.ModelForm):
    date=forms.DateField(
        input_formats=['%d-%m-%Y']
    )
    class Meta:
        model=models.Books
        exclude=['is_active']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']