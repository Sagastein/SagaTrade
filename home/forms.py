from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Item
INPUT_CLASSES = 'w-full px-4 rounded-xl'
class NewItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields = ('category', 'name', 'description', 'price','image')

        widgets = {
            'category': forms.Select(attrs={
            'class': INPUT_CLASSES,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }    


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image','is_solid')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username',
        'class': 'w-full rounded-xl',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'w-full rounded-xl',
    }))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username',
        'class': 'w-full rounded-xl',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your e mail address',
        'class': 'w-full rounded-xl',
    }))
    password1  = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'w-full rounded-xl',
    }))

    password2  = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' repet password Enter your password',
        'class': 'w-full rounded-xl',
    }))
