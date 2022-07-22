from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegistration(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistration, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class Userform(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UserProfilform(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'second_name', 'contact', 'user_image', 'gender']

    def __init__(self, *args, **kwargs):
        super(UserProfilform, self).__init__(*args, **kwargs)
        for fieldname in ['first_name', 'second_name', 'contact', 'user_image', 'gender']:
            self.fields[fieldname].help_text = None


class UserAuthentication(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
