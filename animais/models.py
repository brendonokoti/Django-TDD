from django.db import models

class Animal(models.Model):
    nome_cientifico = models.CharField(max_length=100)
    nome_popular = models.CharField(max_length=100)
    predador = models.BooleanField(default=False)
    venenoso = models.BooleanField(default=False)
    domestico = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_popular