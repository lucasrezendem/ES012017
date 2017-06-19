from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^cadastro/(?P<tipo_evento>.+)/$', views.cadastro_evento, name='cadastro_evento'),
    url(r'^delete/(?P<tipo_evento>.+)/(?P<nome>.+)/$', views.deleta_evento, name='deleta_evento'),
    url(r'^atualiza/(?P<tipo_evento>.+)/(?P<nome>.+)/$', views.atualiza_evento, name='atualiza_evento'),
    url(r'^bares/$', views.view_bares, name='bares'),
    url(r'^festas/$', views.view_festas, name='festas'),
    url(r'^teatro/$', views.view_teatros, name='teatro'),
    url(r'^esportes/$', views.view_esportes, name='esportes'),
]
