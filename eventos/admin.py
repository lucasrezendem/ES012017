from django.contrib import admin
from django.contrib import admin
from .models import bar

class barAdmin(admin.ModelAdmin):
    pass
admin.site.register(bar, barAdmin)
