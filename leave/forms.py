from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class LogLeaveForm(forms.Form):
    startdate = forms.DateField( widget=DateInput())
    enddate=forms.DateField(widget=DateInput() )