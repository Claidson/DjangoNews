# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from NoticiasTabajara.models import *
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render, render_to_response
import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from .forms import UserLoginForm, UserRegisterForm

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
		pagina = int(request.GET.get('pagina', '1'))
	except ValueError:
		pagina = 1
    # Se o page request (9999) está fora da lista, mostre a última página.
	try:
		paginas = paginator.page(pagina)
	except (EmptyPage, InvalidPage):
		paginas = paginator.page(paginator.num_pages)
	return render(request,'NoticiasTabajara/pagina.html', context = {"paginas": paginas})

def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "NoticiasTabajara/form.html", {"form":form, "title": title})


def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "NoticiasTabajara/form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")