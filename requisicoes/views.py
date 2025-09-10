from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Requisicao, Material
from .forms import RequisicaoForm, ItemRequisicaoFormset
from django.urls import reverse
from django.contrib import messages
#from estoque.models import Movimentacao


@login_required
def nova_requisicao(request):
    materiais = Material.objects.all()

    if request.method == 'POST':
        form = RequisicaoForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.requisitante = request.user
            req.save()

            formset = ItemRequisicaoFormset(request.POST, instance=req)
            if formset.is_valid():
                formset.save()
                return redirect('requisicoes:listar')
        else:
            # se o form principal inválido, recria formset para re-render com erros
            formset = ItemRequisicaoFormset(request.POST)
    else:
        form = RequisicaoForm()
        formset = ItemRequisicaoFormset()

    return render(request, 'requisicoes/nova_requisicao.html', {
        'form': form,
        'formset': formset,
        'materiais': materiais,
    })

@login_required
def listar_requisicoes(request):
    if request.user.is_superuser:  
       requisicoes = Requisicao.objects.all().order_by('-data_requisicao')
    else:
       requisicoes = Requisicao.objects.filter(requisitante=request.user)   
    return render(request, 'requisicoes/lista_requisicoes.html', {'requisicoes': requisicoes})



@login_required
def detalhe_requisicao(request, pk):
    if request.user.is_superuser:
       req = get_object_or_404(Requisicao, pk=pk)
    else:
        req = get_object_or_404(Requisicao, pk=pk, requisitante=request.user)   
    return render(request, 'requisicoes/detalhe_requisicao.html', {'requisicao': req})

@login_required
def atender_requisicao(request, pk):
    # Somente superusuários ou staff podem atender
    if not (request.user.is_superuser or request.user.is_staff):
        messages.error(request, "Você não tem permissão para atender requisições.")
        return redirect("requisicoes:detalhe", pk=pk)

    req = get_object_or_404(Requisicao, pk=pk)

    if req.status != "pendente":
        messages.warning(request, "A requisição já foi atendida ou aprovada.")
        return redirect("requisicoes:detalhe", pk=req.pk)

    # Verifica estoque
    for item in req.itens.all():
        if item.quantidade > item.material.quantidade_estoque:
            messages.error(request, f"Estoque insuficiente para {item.material.nome}.")
            return redirect("requisicoes:detalhe", pk=req.pk)

    # Atualiza estoque
    for item in req.itens.all():
        item.material.quantidade_estoque -= item.quantidade
        item.material.save()

    # Atualiza status
    req.status = "atendida"
    req.save()

    messages.success(request, "Requisição atendida e estoque atualizado.")
    return redirect("requisicoes:detalhe", pk=req.pk)