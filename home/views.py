from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuário com essse username')

        user = User.objects.create_user(username=username,password=senha)
        user.save()
        return redirect(login_view)

        
def login_view(request):
    if request.method == "GET":   
        return render(request, 'login.html')
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = authenticate(username=username, password=senha)
        if user:
            login(request, user)

            return redirect (index)
        else:
            return HttpResponse('Usuário ou senha inválida')
        
@login_required(login_url="/auth/login/")
def index(request):
    return render(request, 'home.html')

@login_required(login_url="/auth/login/")
def base(request):
    return render(request, 'base.html')
    
@login_required(login_url="/auth/login/")
def livro_list(request):
    return render(request, 'livro_list.html')

@login_required(login_url="/auth/login/")
def livro_create(request):
    return render(request, 'livro_form.html')

@login_required(login_url="/auth/login/")
def salvar_livro(request, id):
    if request.method == "POST":
        titulo = request.POST.get("nome")
        if titulo == "":
            return render(request, "page_404.html")
        nome_autor = request.POST.get("nome_autor")
        data_publicacao = request.POST.get("data_publicacao")
        if data_publicacao == "":
            data_publicacao = None
        editora = request.POST.get("editora")
        num_pag = request.POST.get("num_pag")
        genero = request.POST.get("genero")
        idioma = request.POST.get("idioma")
        formato = request.POST.get("formato")
        preco = request.POST.get("preco")
        capa = request.POST.get("capa")
        descricao = request.POST.get("descricao")

        Livro.objects.create(
            titulo=titulo,
            autor=nome_autor,
            data_publicacao=data_publicacao,
            editora=editora,
            numero_paginas=num_pag,
            genero=genero,
            idioma=idioma,
            descricao=descricao,
            capa=capa,
            formato=formato,
            preco=preco,    
        )
        return redirect(livro_list)
    return redirect(salvar_livro)
    
@login_required(login_url="/auth/login/")
def editar_livro(request, id):
    livros = Livro.objects.get(id=id)
    return render(request, "editar_equipe.html", {"livros": livros})

@login_required(login_url="/auth/login/")
def update_livro(request, id):
    nome = request.POST.get("nome")
    equipes = Livro.objects.get(id=id)
    equipes.nome = nome
    equipes.save()
    return redirect(livro_list)

@login_required(login_url="/auth/login/")
def delete_livro(request, id):
    livro = Livro.objects.get(id=id)
    livro.delete()
    return redirect(livro_list)

    