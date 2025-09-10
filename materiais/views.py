from django.shortcuts import render, get_object_or_404
from .models import Material


def lista_materiais(request):
    materiais = Material.objects.all()
    return render(request, 'materiais/lista.html', {'materiais': materiais})


def material_detalhe(request, pk):
    m = get_object_or_404(Material, pk=pk)
    return render(request, 'materiais/detalhe.html', {'material': m})