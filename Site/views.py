from django.shortcuts import render
from Site.forms import ClienteForm

from Site.models import Departamento, Produto, Cliente

# Create your views here.

def index(request):
    produtos_em_destaque = Produto.objects.filter(destaque = True)
    context = {
        'produtos' : produtos_em_destaque,
    }
    return render(request,'index.html', context)

def produto_lista(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
        'nome_categoria' : "Todos os Produtos"
    }
    return render(request, 'produtos.html', context)

def produto_detalhe(request, id):
    produto_selecionado = Produto.objects.get(id = id)
    produtos_relacionados = Produto.objects.filter(departamento_id = produto_selecionado.departamento.id)
    context = {
        'produto_selecionado': produto_selecionado,
        'produtos_relacionados': produtos_relacionados
    }
    return render(request, 'produto_detalhes.html', context)

def institucional(request):
    return render(request, 'empresa.html')

def cadastro(request):
    formulario = ClienteForm()
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            cliente = formulario.save()
            formulario = ClienteForm()
    else:
        formulario = ClienteForm()
    context = {
        'form_cliente':formulario
    }
    return render(request, 'cadastro.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto_lista_por_id(request, id):
    departamentos = Departamento.objects.all()
    produtos_por_departamento = Produto.objects.filter(departamento_id = id)
    categoria = departamentos.get(id = id).nome
    context = {
        'departamentos': departamentos,
        'produtos': produtos_por_departamento,
        'nome_categoria': categoria
    }
    return render(request, 'produtos.html', context)