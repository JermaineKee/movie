from django import forms
from django.contrib.auth.models import User
from movieapp.models import Rater


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class RaterForm(forms.ModelForm):

    class Meta:
        model = Rater
        fields = ('age', 'gender', 'occupation', 'zipcode')
