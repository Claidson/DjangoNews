from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^index',views.index, name='index'),
    url(r'^cadastrarnoticia',views.cad, name='cad'),
    url(r'^pagina',views.pagina, name='pagina'),
    url(r'^noticias/(?P<noticia_id>[0-9]+)', views.noticias, name='noticias'),
    
]

