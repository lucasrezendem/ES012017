from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pagina_bares/$', views.bares, name='bares'),
    url(r'^pagina_esportes/$', views.esportes, name='esportes'),
	url(r'^pagina_festas/$', views.festas, name='festas'),
	url(r'^pagina_sobre/$', views.sobre, name='sobre'),
	url(r'^pagina_teatro/$', views.teatro, name='teatro'),
	url(r'^fazerlogin/$', views.fazerlogin, name='fazerlogin'),
	url(r'^fazersignup/$', views.fazersignup, name='fazersignup'),
	url(r'^login/$', views.login, name='login'),
	url(r'^about/$', views.about, name='about'),

]
