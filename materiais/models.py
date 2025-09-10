from django.db import models


class Material(models.Model):

    codigo = models.CharField(max_length=20, unique=True)  # código único do material
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    imagem = models.ImageField(upload_to='materiais/', blank=True, null=True)
    unidade_medida = models.CharField(max_length=50, default='un')
    quantidade_estoque = models.PositiveIntegerField(default=0)


class Meta:

    verbose_name = 'Material'
    verbose_name_plural = 'Materiais'
    ordering = ['nome']


def __str__(self):

    return f"{self.nome} ({self.codigo}) - ({self.quantidade_estoque} {self.unidade_medida})"

