# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    	return render(request,'NoticiasTabajara/index.html')

def cad(request):
    	return render(request,'NoticiasTabajara/CadastrarNoticia.html')
