from django.contrib.auth.models import User
from django.db import models
from core.models import TimeStampedModel
from produto.models import Produto

MOVIMENT = (
    ('e', 'entrada'),
    ('s', 'saída'),
)

class Estoque(TimeStampedModel):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField('Nota Fiscal', null=True, blank=True)
    moviment = models.CharField(max_length=1, choices=MOVIMENT)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.pk)
    

class EstoqueItens(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.pk} - {self.estoque.pk} - {self.produto}'
    