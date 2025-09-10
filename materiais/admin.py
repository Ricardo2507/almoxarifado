from django.contrib import admin
from .models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'quantidade_estoque', 'unidade_medida')
    search_fields = ('nome', 'categoria')