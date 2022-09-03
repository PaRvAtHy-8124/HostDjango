from socket import fromshare
from django import forms
from . models import Details, Image_det

class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,min_length=3,max_length=8)
    class Meta():
        model=Details
        fields=('Email','Password')

class ImageForm(forms.ModelForm):
    class Meta():
        model=Image_det
        fields='__all__'