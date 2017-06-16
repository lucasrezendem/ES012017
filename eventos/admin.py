from django.contrib import admin
from django.contrib import admin
from .models import *

class barAdmin(admin.ModelAdmin):
    pass
admin.site.register(bar, barAdmin)


class esporteAdmin(admin.ModelAdmin):
    pass
admin.site.register(esporte, esporteAdmin)


class festaAdmin(admin.ModelAdmin):
    pass
admin.site.register(festa, festaAdmin)


class teatroAdmin(admin.ModelAdmin):
    pass
admin.site.register(teatro, teatroAdmin)
