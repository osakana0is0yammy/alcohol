from django import forms
from .models import First,Second,Third,Fourth,Fifth,Sixth,Seventh,Eighth,Title,Odai,Content
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class OdaiForm(forms.ModelForm):
    class Meta:
        model = Odai
        fields = ('odai',)
        labels = {
            'odai':'タイトル入力',

        }

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('content',)
        labels = {
            'content' : 'ゲーム内容を入力してください．',
        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass