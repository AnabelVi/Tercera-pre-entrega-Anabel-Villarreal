from django import forms

class AvionFormulario(forms.Form):

    marca = forms.CharField()
    matricula = forms.IntegerField()