from django.db import models

from django.db import models
from django.conf import settings
from materiais.models import Material


class Requisicao(models.Model):
    STATUS_CHOICES = (
    ('pendente', 'Pendente'),
    ('aprovada', 'Aprovada'),
    ('atendida', 'Atendida'),
)
    requisitante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_requisicao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')


def __str__(self):
    return f"Requisição #{self.id} - {self.requisitante.username} ({self.status})"


class ItemRequisicao(models.Model):
    requisicao = models.ForeignKey(Requisicao, on_delete=models.CASCADE, related_name='itens')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()


def __str__(self):
    return f"{self.material.nome} x {self.quantidade}"
