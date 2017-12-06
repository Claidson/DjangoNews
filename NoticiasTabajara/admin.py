# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from NoticiasTabajara.models import Pagina, Noticia, Imagen, Editor, Comentario, AccessRecord

admin.site.register(Pagina)
admin.site.register(Noticia)
admin.site.register(Imagen)
admin.site.register(Editor)
admin.site.register(Comentario)
admin.site.register(AccessRecord)

# Register your models here.
