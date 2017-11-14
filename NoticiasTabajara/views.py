# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from NoticiasTabajara.models import *
from django.shortcuts import redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render, render_to_response
import forms

# Create your views here.
def index(request):
	lista_noticias = Noticia.objects.order_by('data')
	return render(request,'NoticiasTabajara/index.html', context = {"noticias":lista_noticias})    

def cad(request):
	form = forms.CadastrarNoticia()
	if request.method == 'POST':
		pDict = request.POST.copy()    	
		form = forms.CadastrarNoticia(pDict,request.FILES)
		if form.is_valid():
			print("Cadastrado!")	
			novanoticia = Noticia.objects.get_or_create(titulo=form.cleaned_data['titulo'],data=form.cleaned_data['data'],resumo=form.cleaned_data['resumo'],texto=form.cleaned_data['texto'],imagem=form.cleaned_data['imagem'])
			form = forms.CadastrarNoticia()
	return render(request,'NoticiasTabajara/CadastrarNoticia.html', {'form':form})

def noticias(request, noticia_id):
   noticia = Noticia.objects.get(id=noticia_id)
   return render(request,'NoticiasTabajara/noticia.html', context = {"noticia":noticia})

def pagina(request):
	pagina_lista = Noticia.objects.order_by('data')
	paginator = Paginator(pagina_lista, 1)
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
    # Se o page request (9999) está fora da lista, mostre a última página.
	try:
		paginas = paginator.page(page)
	except (EmptyPage, InvalidPage):
		paginas = paginator.page(paginator.num_pages)
	return render(request,'NoticiasTabajara/pagina.html', context = {"paginas": paginas})
