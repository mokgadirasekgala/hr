from django import forms

class LogLeaveForm(forms.Form):
    startdate = forms.CharField(label='startdate', max_length=100)
    enddate=forms.CharField(label='enddate', max_length=100)