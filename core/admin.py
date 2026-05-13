from django.contrib import admin
from .models import Persona

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ("name", "apellidos", "email", "create")
    search_fields = ("name", "apellidos", "email", "create")
    readonly_fields = ("create", "update")

admin.site.register(Persona, PersonaAdmin)

