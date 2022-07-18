from django import forms
from .models import *


class UserDetailUpdate(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UserProfileUpdate(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'second_name', 'contact', 'user_image', 'gender')

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdate, self).__init__(*args, **kwargs)
        for fieldname in ['first_name', 'second_name', 'contact', 'user_image', 'gender']:
            self.fields[fieldname].help_text = None
