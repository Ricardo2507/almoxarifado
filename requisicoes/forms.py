from django import forms
from .models import Requisicao, ItemRequisicao
from materiais.models import Material


class ItemRequisicaoForm(forms.ModelForm):
    class Meta:
        model = ItemRequisicao
        fields = ('material', 'quantidade')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        qs = Material.objects.all()
        self.fields['material'].queryset = qs
        # força o rótulo exibido na <option>
        self.fields['material'].label_from_instance = lambda obj: f"{obj.nome} ({obj.quantidade_estoque} {obj.unidade_medida})" 


ItemRequisicaoFormset = forms.inlineformset_factory(
    Requisicao, ItemRequisicao, form=ItemRequisicaoForm, extra=1, can_delete=True
)


class RequisicaoForm(forms.ModelForm):
    class Meta:
        model = Requisicao
        fields = [] # requisitante populado no view