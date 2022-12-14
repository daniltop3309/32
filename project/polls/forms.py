from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    country = forms.CharField()
    region = forms.CharField()
    street = forms.CharField()