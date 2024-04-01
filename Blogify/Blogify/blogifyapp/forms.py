from django import forms
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User


class usersForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs = {'class':"form-control"}))
    username = forms.CharField(widget= forms.TextInput(attrs = {'class':"form-control"}))
    Email_Address = forms.CharField(widget =forms.EmailInput(attrs = {'class':"form-control"}))
    password1 = forms.CharField(label = "Your password", widget= forms.TextInput(attrs= {'class':"form-control"}))
    password2 = forms.CharField(label = "Confirm Password",widget= forms.TextInput(attrs= {'class':"form-control"}))
    

    

