from django.shortcuts import render

from Site.models import Departamento, Produto

# Create your views here.

def index(request):
    return render(request,'index.html')

def produto_lista(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
        'nome_categoria' : "Todos os Produtos"

    }
    return render(request, 'produtos.html', context)

def produto_detalhe(request, id):
    return render(request, 'produto_detalhes.html')

def institucional(request):
    return render(request, 'empresa.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def contato(request):
    return render(request, 'contato.html')

def produto_lista_por_id(request, id):
    return render(request, 'produtos.html')
