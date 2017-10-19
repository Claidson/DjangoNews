# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
import forms

# Create your views here.
def index(request):
    	
    	return render(request,'NoticiasTabajara/index.html')

def cad(request):
	form = forms.CadastrarNoticia()
	if request.method == 'POST':
		form = forms.CadastrarNoticia(request.POST)
		if form.is_valid():
			print("Validation susses!")
	return render(request,'NoticiasTabajara/CadastrarNoticia.html', {'form':form})