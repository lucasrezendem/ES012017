from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^cadastro/(?P<tipo_evento>.+)/$', views.cadastro_evento, name='cadastro_evento'),
    url(r'^pagina_bares/$', views.bares, name='bares'),
    url(r'^pagina_festas/$', views.festas, name='festas'),
    url(r'^pagina_teatro/$', views.teatro, name='teatro'),
    url(r'^pagina_esportes/$', views.esportes, name='esportes'),
]
