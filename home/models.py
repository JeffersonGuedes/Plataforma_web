from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    senha = models.CharField(max_length=20)

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255, blank=True, null=True)
    data_publicacao = models.DateField(blank=True, null=True)
    editora = models.CharField(max_length=255, blank=True, null=True)
    numero_paginas = models.IntegerField(blank=True, null=True)
    genero = models.CharField(max_length=100, blank=True, null=True)
    idioma = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    formato = models.CharField(max_length=50, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_adicao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='livros')

    def __str__(self):
        return self.titulo