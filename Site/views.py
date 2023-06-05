from django.shortcuts import render
from Site.forms import ClienteForm, ContatoForm
from Site.models import Departamento, Produto, Cliente
from django.core.mail import send_mail

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
    mensagem =""
    formulario = ClienteForm()
    #quando faço clique no botão de enviar
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid(): #faz todas as validações
            cliente = formulario.save() #salva dados na tabela
            formulario = ClienteForm() #formulário vazio é devolvido
            mensagem = "Cliente cadastrado com sucesso"
    else: #quando carrego a página vazia
        formulario = ClienteForm()
    context = {
        'form_cliente':formulario,
        'mensagem': mensagem
    }
    return render(request, 'cadastro.html', context)

def contato(request):
    mensagem = ""
    if request.method == "POST":
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        assunto = request.POST['assunto']
        mensagem = request.POST['mensagem']
        remetente = request.POST['email']
        destinatario = ['contato@shopping.com.br']
        corpo = f"Nome: {nome} \nTelefone: {telefone}  \nMensagem: {mensagem}"
    
        try:
            send_mail(assunto, corpo, remetente, destinatario)
            mensagem = 'E-mail enviado com sucesso!'
        except:
            mensagem = 'Erro ao enviar e-mail!'
    
    formulario = ContatoForm()

    context = {
        'form_contato' : formulario,
        'mensagem' : mensagem
    }
    return render(request, 'contato.html', context)

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