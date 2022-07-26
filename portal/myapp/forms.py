from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, UserEducatioDetail


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


class userprofileform(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(userprofileform, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'first_name', 'last_name']:
            self.fields[fieldname].help_text = None


class Userdetailsform(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['gender', 'contact', 'user_image']

    def __init__(self, *args, **kwargs):
        super(Userdetailsform, self).__init__(*args, **kwargs)
        for fieldname in ['gender', 'contact', 'user_image']:
            self.fields[fieldname].help_text = None


class UserEducation(forms.ModelForm):
    class Meta:
        model = UserEducatioDetail
        exclude = ('user',)
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserEducation, self).__init__(*args, **kwargs)
        for fieldname in ['__all__']:
            self.fields[fieldname].help_text = None


class UserEducationCreate(forms.ModelForm):
    class Meta:
        model = UserEducatioDetail
        fields = ['cert_degree_name', 'institution_name', 'completion_date', 'starting_date']

    def __init__(self, *args, **kwargs):
        super(UserEducationCreate, self).__init__(*args, **kwargs)
        for fieldname in ['cert_degree_name', 'institution_name', 'completion_date', 'starting_date']:
            self.fields[fieldname].help_text = None


class UserAuthentication(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
