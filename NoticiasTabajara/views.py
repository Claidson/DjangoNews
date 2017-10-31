# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from NoticiasTabajara.models import *

from django.shortcuts import render
import forms

# Create your views here.
def index(request):
	lista_noticias = Noticia.objects.order_by('titulo')
	return render(request,'NoticiasTabajara/index.html', context = {"noticias":lista_noticias})    

def cad(request):
	form = forms.CadastrarNoticia()
	if request.method == 'POST':
		form = forms.CadastrarNoticia(request.POST)
		if form.is_valid():
			print("Validation susses!")	
			novanoticia = Noticia.objects.get_or_create(titulo=form.cleaned_data['titulo'],data=form.cleaned_data['data'],resumo=form.cleaned_data['resumo'],texto=form.cleaned_data['texto'])
			

	return render(request,'NoticiasTabajara/CadastrarNoticia.html', {'form':form})