from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.pagina, name='index'),
    url(r'^index',views.pagina, name=''),
    url(r'^cadastrarnoticia',views.cad, name='cad'),
    url(r'^pagina',views.pagina, name='pagina'),
    url(r'^noticias/(?P<noticia_id>[0-9]+)', views.noticias, name='noticias'),
    url(r'^register/', views.register_view, name='register'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    
]

