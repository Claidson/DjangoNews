# -*- coding: utf-8 -*- 
from django import forms

class CadastrarNoticia(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    resumo = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))
    data = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    texto = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))
    imagem = forms.ImageField()

    def __str__(self):
        return self.titulo