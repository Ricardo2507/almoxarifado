from django.contrib import admin
from .models import Requisicao, ItemRequisicao


class ItemInline(admin.TabularInline):
    model = ItemRequisicao
    extra = 1


@admin.register(Requisicao)
class RequisicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'requisitante', 'status', 'data_requisicao')
    inlines = [ItemInline]