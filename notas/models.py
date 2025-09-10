from django.db import models
from django.utils import timezone
from materiais.models import Material  # Importa Material da outra app

class NotaFiscal(models.Model):
    numero = models.CharField(max_length=50, unique=True)
    data = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Nota {self.numero} - {self.data}"


class ItemNotaFiscal(models.Model):
    nota_fiscal = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE, related_name='itens')
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()

    # Atualiza estoque automaticamente
    def save(self, *args, **kwargs):
        if self.pk:
            antigo = ItemNotaFiscal.objects.get(pk=self.pk)
            diferenca = self.quantidade - antigo.quantidade
            self.material.quantidade_estoque += diferenca
        else:
            self.material.quantidade_estoque += self.quantidade
        self.material.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.material.quantidade_estoque -= self.quantidade
        self.material.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.material.nome} - {self.quantidade} {self.material.unidade_medida}"
