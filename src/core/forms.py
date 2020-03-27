from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Music, Repertory, RepertoryMusic


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User


class NewMusicForm(forms.Form):
    name = forms.CharField(max_length=200)
    artist = forms.CharField(max_length=200)
    yt_link = forms.CharField(max_length=200)

    class Meta:
        model = Music


class CreateRepertoryForm(forms.Form):
    name = forms.CharField(max_length=200)
    note = forms.CharField(max_length=500)

    class Meta:
        model = Repertory


class AddMusicForm(forms.ModelForm):

    class Meta:
        model = RepertoryMusic
        fields = ['rehearsed', 'music', 'tonality', 'note']

class UpdateMusicForm(forms.ModelForm):

    class Meta:
        model = RepertoryMusic
        fields = ['rehearsed', 'tonality', 'note']
        