from django.contrib import admin
from .models import Desktops

# Register your models here.

#@admin.register(Desktops)
class AuthorAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


admin.site.register(Desktops, AuthorAdmin)