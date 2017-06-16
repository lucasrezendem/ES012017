from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^cadastro/(?P<tipo_evento>.+)/$', views.cadastro_evento, name='cadastro_evento'),
    url(r'^delete/(?P<tipo_evento>.+)/(?P<nome>.+)/$', views.deleta_evento, name='deleta_evento'),
    url(r'^atualiza/(?P<tipo_evento>.+)/(?P<nome>.+)/$', views.atualiza_evento, name='atualiza_evento'),
    url(r'^bares/$', views.bares, name='bares'),
    url(r'^festas/$', views.festas, name='festas'),
    url(r'^teatro/$', views.teatro, name='teatro'),
    url(r'^esportes/$', views.esportes, name='esportes'),
]
