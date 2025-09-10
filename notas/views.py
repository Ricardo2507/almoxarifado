# notas/views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import NotaFiscal, ItemNotaFiscal
from .forms import NotaFiscalForm, ItemNotaFiscalForm,ItemNotaFiscalFormset
from .models import NotaFiscal



@login_required
def nova_nota_fiscal(request):
    if request.method == 'POST':
        form = NotaFiscalForm(request.POST)
        if form.is_valid():
            nota = form.save()
            formset = ItemNotaFiscalFormset(request.POST, instance=nota)
            if formset.is_valid():
                formset.save()
                return redirect('notas:listar')  # substitua pela sua URL
        else:
            # Se o form for inválido, cria formset para renderizar
            formset = ItemNotaFiscalFormset(request.POST)
    else:
        form = NotaFiscalForm()
        formset = ItemNotaFiscalFormset()

    return render(request, 'notas/nova_nota_cards.html', {
        'form': form,
        'formset': formset,
    })

@login_required
def adicionar_item_nota(request):
    """
    Retorna um novo form parcial de ItemNotaFiscal para ser adicionado dinamicamente via HTMX.
    """
    form_index = request.GET.get('form_index', 0)
    form = ItemNotaFiscalForm(prefix=f'itens-{form_index}')
    return render(request, 'notas/item_nota_form.html', {'form': form})
@login_required
def listar_notas(request):
    # Lista todas as notas fiscais, ordenadas pela mais recente
    notas = NotaFiscal.objects.all().order_by('-data')
    return render(request, 'notas/listar_notas.html', {'notas': notas})

# notas/views.py
@login_required
def detalhe_nota(request, pk):
    # Busca a nota pelo id (pk) ou retorna 404 se não existir
    nota = get_object_or_404(NotaFiscal, pk=pk)
    return render(request, 'notas/detalhe_nota.html', {'nota': nota})
