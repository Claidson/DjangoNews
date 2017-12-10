# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.

class Editor(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome


class Imagen(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    caminho = models.ImageField(upload_to='static/images', default='static/images/django.jpg')

    # https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield

    def __str__(self):
        return self.nome


class Pagina(models.Model):
    nome = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.nome


class AccessRecord(models.Model):
    pagina = models.ForeignKey(Pagina)
    data = models.DateField()

    def __str__(self):
        return str(self.data)


class Noticia(models.Model):
    data = models.DateField()
    texto = models.TextField()
    titulo = models.CharField(max_length=100)
    resumo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='fotos/%Y/%m/%d', default='static/images/django.jpg')

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    data = datetime.now()
    texto = models.CharField(max_length=200, null=True)
    nome = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    active_status = models.BooleanField(default=0)
    noticia_fk = models.ForeignKey(Noticia, null=True)

    def is_active(self):
        return bool(self.active_status)

    def __str__(self):
        return str(self.nome)
