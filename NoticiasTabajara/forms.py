# -*- coding: utf-8 -*-
from bootstrap_datepicker.widgets import DatePicker
from django import forms

class CadastrarNoticia(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    resumo = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))
    data = forms.DateField(widget=DatePicker(options={"format": "dd/mm/yyyy","autoclose": True}))
    texto = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))

    def __str__(self):
        return self.titulo