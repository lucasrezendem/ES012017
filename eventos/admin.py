from django.contrib import admin
from django.contrib import admin
from .models import *

@admin.register(bar)
class barAdmin(admin.ModelAdmin):
    """ Registra o model bar no menu de administrador. """
    pass


@admin.register(esporte)
class esporteAdmin(admin.ModelAdmin):
    """ Registra o model esporte no menu de administrador. """
    pass


@admin.register(festa)
class festaAdmin(admin.ModelAdmin):
    """ Registra o model festa no menu de administrador. """
    pass


@admin.register(teatro)
class teatroAdmin(admin.ModelAdmin):
    """ Registra o model teatro no menu de administrador. """
    pass
