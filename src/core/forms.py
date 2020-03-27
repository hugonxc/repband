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


class AddMusicForm(forms.Form):
    CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)

    rehearsed = forms.BooleanField(required=False)
    music = forms.ModelChoiceField(queryset=Music.objects.all(), to_field_name="id")
    tonality = forms.ChoiceField(choices=RepertoryMusic.TONALITES)
    note = forms.CharField(max_length=500, required=False)

    class Meta:
        model = RepertoryMusic