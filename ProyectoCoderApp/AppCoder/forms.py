from django import forms

class AvionFormulario(forms.Form):

    marca = forms.CharField()
    matricula = forms.CharField()

class PilotoFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    rango = forms.CharField(max_length=50)