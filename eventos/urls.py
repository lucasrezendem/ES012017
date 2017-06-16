from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^cadastro/(?P<tipo_evento>.+)/$', views.cadastro_evento, name='cadastro_evento'),
]
