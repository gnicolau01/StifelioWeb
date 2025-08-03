from django.forms import ModelForm
from .models import *
from .models import Review
from django import forms


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'rating']