from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.core import validators


class SignForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                                    'class': 'form-control mb-4',
                                                                                    }))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                                                 'class': 'form-control mb-4',
                                                                                                 }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email']
        labels = {'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Exists")

        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3:
            raise forms.ValidationError(
                "Your Name Is Too Short It Should Be Greater Than 2")
        return first_name


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username", widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username', 'class': 'form-control form-control-sm mb-4'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password',
                                                                                   'class': 'form-control form-control-sm mb-4',
                                                                                   }))

    class Meta:
        model = User
        fields = ['username', 'password']
