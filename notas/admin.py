# notas/admin.py
from django.contrib import admin
from .models import NotaFiscal, ItemNotaFiscal

class ItemNotaFiscalInline(admin.TabularInline):
    model = ItemNotaFiscal
    extra = 1

@admin.register(NotaFiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    list_display = ('numero', 'data', 'total_itens')
    search_fields = ('numero',)
    inlines = [ItemNotaFiscalInline]

    def total_itens(self, obj):
        return obj.itens.count()
    total_itens.short_description = 'Total de Itens'

@admin.register(ItemNotaFiscal)
class ItemNotaFiscalAdmin(admin.ModelAdmin):
    list_display = ('nota_fiscal', 'material', 'quantidade')
    search_fields = ('nota_fiscal__numero', 'material__nome')
