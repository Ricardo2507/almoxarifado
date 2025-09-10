from django.contrib import admin
from .models import Movimentacao

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ("material", "tipo", "quantidade", "data", "usuario")
    list_filter = ("tipo", "data")
    search_fields = ("material__nome", "usuario__username")
