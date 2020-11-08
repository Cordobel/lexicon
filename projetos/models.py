import datetime

from django.db import models
from django.utils import timezone

class Projetos(models.Model):
    nome_do_projeto = models.CharField(max_length=200)
    data_inicio = models.DateTimeField('Iniciado')
    data_fim = models.DateTimeField('Finalizado')

    class Meta:
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.nome_do_projeto

class Atividades(models.Model):
    id_projeto = models.ForeignKey(Projetos, on_delete=models.CASCADE)
    nome_atividade = models.CharField(max_length=200)
    data_inicio = models.DateTimeField('Iniciar')
    data_fim = models.DateTimeField('Finalizar')
    finalizada = models.BooleanField()

    class Meta:
        verbose_name_plural = "Atividades"

    def __str__(self):
        return self.nome_atividade
