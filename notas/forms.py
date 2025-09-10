from django import forms
from django.forms import inlineformset_factory
from .models import NotaFiscal, ItemNotaFiscal
from materiais.models import Material

# ModelChoiceField customizado para mostrar "código - nome"
class MaterialChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.codigo} - {obj.nome}"

# Form principal da Nota Fiscal
class NotaFiscalForm(forms.ModelForm):
    class Meta:
        model = NotaFiscal
        fields = ('numero', 'data')

# Form dos Itens da Nota Fiscal
class ItemNotaFiscalForm(forms.ModelForm):
    material = MaterialChoiceField(queryset=Material.objects.all())

    class Meta:
        model = ItemNotaFiscal
        fields = ('material', 'quantidade')

# Inline formset
ItemNotaFiscalFormset = inlineformset_factory(
    NotaFiscal,
    ItemNotaFiscal,
    form=ItemNotaFiscalForm,
    extra=1,
    can_delete=True
)
