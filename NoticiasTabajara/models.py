# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Noticia(models.Model):
    nome = models.CharField(max_length=264, unique=True)
    data = models.DateField()
    texto = models.CharField(max_length = 500)
    titulo = models.CharField(max_length = 100)
    resumo = models.CharField(max_length = 200)
    pagina = models.ForeignKey(Pagina)
    imagens =models.ForeignKey(Imagem)
    editor = models.ForeignKey(Editor)
    comentarios = [models.ForeignKey(Comentario)]

    def __str__(self):
        return self.nome

class Pagina(models.Model):
    topic = models.ForeignKey(Topic)
    nome = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.nome

class AccessRecord(models.Model):
    pagina = models.ForeignKey(Pagina)
    data = models.DateField()

    def __str__(self):
        return str(self.data)

class Editor(models.Model):
    nome = models.CharField(max_length = 50, unique=True)
    
    def __str__(self):
        return self.nome

class Imagem(models.Model):
    nome = models.CharField(max_length = 50, unique=True)
    caminho = models.ImageField(upload_to = 'static/images', default = 'static/images/django.jpg')
    # https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield
    
    def __str__(self):
        return self.nome 

class ImageUploadForm(forms.Form):

    image = forms.ImageField()

class Leitor(models.Model):
    nome = models.CharField(max_length = 50, unique=True)
    email = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.nome

class Comentario(models.Model):
    leitor = models.ForeignKey(Leitor)
    data = models.DateField()
    texto = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.data)




 