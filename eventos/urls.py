from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^cadastro(?P<tipo_evento>[0-9]+)/$', views.cadastro, name='cadastro'),
]
