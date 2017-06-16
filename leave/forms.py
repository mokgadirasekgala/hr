from django import forms
from functools import partial
from django.contrib.auth.forms import AuthenticationForm
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class LogLeaveForm(forms.Form):
    startdate = forms.DateField( widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    enddate=forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

class CreateEmployeeForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    firstname=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    lastname=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'pasword'}))
    startdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'pasword'}))
