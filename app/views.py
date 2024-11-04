from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})

def salvar(request):
    nome = request.POST.get('nome')
    Pessoa.objects.create(nome=nome) #o nome do meu modelo recebe o nome inserido no input, o create() irá criar um novo no db
    pessoas = Pessoa.objects.all() # apos criar uma nova pessoa eu pego toda a lista atualizada e mando de volta pro template com o novo item adicionado
    return render(request, 'index.html', {'pessoas':pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'update.html', {'pessoa':pessoa})

def update(request, id):
    nome = request.POST.get('nome')
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = nome
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)
    