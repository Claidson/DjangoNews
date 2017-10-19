# -*- coding: utf-8 -*-
from django import forms

class CadastrarNoticia(forms.Form):

    titulo = forms.CharField()
    resumo = forms.CharField(widget=forms.Textarea)
    data = forms.DateField(input_formats='%d/%m/%Y')
    texto = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return self.titulo