from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class LogLeaveForm(forms.Form):
    startdate = forms.DateField( widget=DateInput())
    enddate=forms.DateField(widget=DateInput() )

class CreateEmployeeForm(forms.Form):
    username=forms.CharField(max_length=30,widget=forms.TextInput())
    firstname=forms.CharField(widget=forms.TextInput())
    lastname=forms.CharField(widget=forms.TextInput())
    email=forms.CharField(widget=forms.EmailInput())
    password=forms.CharField(widget=forms.PasswordInput())
    startdate=forms.DateField( widget=DateInput())

