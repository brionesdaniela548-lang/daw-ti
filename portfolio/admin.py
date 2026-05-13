from django.contrib import admin

# Register your models here.
from .models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ('create','update')

admin.site.register(Portfolio, PortfolioAdmin) #el modelo portfolio se registre en el admin



