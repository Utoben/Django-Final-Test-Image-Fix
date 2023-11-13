from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task",]
        widgets = {
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Введите название поста',
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание поста',
            }),
        }

class PostForm(ModelForm):

    tag = forms.ModelChoiceField(queryset=Tags.objects.all(), initial=Tags.objects.first(), required=False, widget=forms.Select(attrs={'id' : 'tags_id', 'class' : 'custom-select'}))

    class Meta:
        model=Post
        fields=["title","post"]
        widgets={
            "title": TextInput(attrs={
                'class' : 'form-control',
                'id' : 'title_id',
                'placeholder' : 'Придумайте название своего поста'
            }),
            "post": Textarea(attrs={
                'class' : 'form-control',
                'id' : 'post_id',
                'placeholder' : 'Придумайте описание своего поста'
            }),
            "tags_choose": forms.Select(attrs={
               'class' : 'selectpicker',
                'type' : 'text',
                'name' : 'tags_choose',
                'id' : 'tags_choose_id',
            }),
        }

class RegisterUserform(UserCreationForm):
    username = forms.CharField(label='Логин', widget = forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите имя', 'name' : 'full_name', 'id' : 'full_name_id'}))
    password1 = forms.CharField(label='Логин', widget = forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите пароль', 'name' : 'password1', 'id' : 'password1_id'}))
    password2 = forms.CharField(label='Логин', widget = forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Повторите пароль', 'name' : 'password2', 'id' : 'password1_id'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widjets = {
            'username' : forms.TextInput(attrs={
                'type' : 'text',
                'class': 'form-control',
                'placeholder': 'Введите имя',
                'name': 'full_name',
                'id': 'full_name_id',
            }),
            'password1': forms.PasswordInput(attrs={
                'type' : 'text',
            'class': 'form-control',
            'placeholder': 'Введите пароль',
            'name': 'password1',
            'id': 'password1_id',
            }),
            'password2': forms.PasswordInput(attrs={
                'type' : 'text',
            'class': 'form-control',
            'placeholder': 'Повторите пароль',
            'name': 'password2',
            'id': 'password2_id',
            }),
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget = forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите имя', 'name' : 'full_name', 'id' : 'full_name_id'}))
    password = forms.CharField(label='Логин', widget = forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите пароль', 'name' : 'password', 'id' : 'password_id'}))

    class Meta:
        fields = ('username', 'password')
        widjets = {
            'username' : forms.TextInput(attrs={
                'type' : 'text',
                'class': 'form-control',
                'placeholder': 'Введите имя',
                'name': 'full_name',
                'id': 'full_name_id',
            }),
            'password': forms.PasswordInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите пароль',
                'name': 'password',
                'id': 'password_id',
            }),
        }