from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Cliente, Produto
from .forms import ClienteModel, ProdutoModel


def index(request):
    return render(request, 'index.html')


def new_produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModel(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso')
            form = ProdutoModel()
            return redirect('produto')
        else:
            messages.error(request, 'Erro ao cadastrar o produto')
    else:
        form = ProdutoModel()

    context = {'form': form}
    return render(request, 'new_produto.html', context)


def produtos(request):
    produto = Produto.objects.all().order_by('-id')
    paginator = Paginator(produto, 5)
    page = request.GET.get('page')
    produto = paginator.get_page(page)
    context = {'produto': produto}
    return render(request, 'produto.html', context)


def update_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoModel(request.POST or None, instance=produto)
    if form.is_valid():
        produto = form.save()
        produto.save()
        return redirect('produto')
    context = {'form': form}
    return render(request, 'update_produto.html', context)


def delete_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('produto')
    context = {'produto': produto}
    return render(request, 'delete_produto.html', context)



def cliente(request):

    # instncia o model e ordena a listagem por o ultimo elemento cadastrado
    clientes = Cliente.objects.all().order_by('-id')
    # paginação
    paginator = Paginator(clientes, 6)
    page = request.GET.get('page')
    clientes = paginator.get_page(page)
    context = {'cliente': clientes}
    return render(request, 'cliente.html', context)


def new_cliente(request):
    # verifica se o methodo da request for post
    if str(request.method) == 'POST':
        # o form vai ser o seguinte abaixo
        form = ClienteModel(request.POST or None)
        # valida, se o form for valido, com todos seus campos preenchidos com os tipos de dados
        if form.is_valid():
            # salvoo form no banbo de dados
            form.save()
            # exibe uma mensagem de sucesso
            messages.success(request, 'Cadastrado com sucesso')
            # apos o form ser salvo com sucesso, o form é instanciado novamente retornando um form vazio
            form = ClienteModel()
            # retona e redireciona para a url cliente da listagem de clientes
            return redirect('cliente')
        # se o form nao for salvo, ocorrer algum erro
        else:
            # exibe a menssagem de erro
            messages.error(request, 'Erro ao cadastrar')
    # se o form não for do tipo 'POST', ele ira renderizar a pagina
    else:
        # instanciar um ModelForm, e criar um formulario limpo em branco
        form = ClienteModel()
    # colocara o contexto detro da pagina html
    context = {
        'form': form
    }
    # e retornara renderizando para a pagina do formulario com o contexto dentro
    return render(request, 'new_cliente.html', context)


def cliente_update(request, id):
    clientes = get_object_or_404(Cliente, id=id)
    form = ClienteModel(request.POST or None, instance=clientes)
    if form.is_valid():
        clientes = form.save()
        clientes.save()
        return redirect('cliente')
    context = {'form': form}

    return render(request, 'update_cliente.html', context)


def cliente_detail(request, id):
    clientes = get_object_or_404(Cliente, pk=id)
    context = {'clientes': clientes}
    return render(request, 'detail_cliente.html', context)


def cliente_delete(request, id):
    clientes = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        clientes.delete()
        return redirect('cliente')
    context = {'clientes': clientes}

    return render(request, 'delete_cliente.html', context)









    """
    Esse modelo é utilizado para formulario de contata,
    que não necessita salvar no banco de dados

    form = ClienteForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            sexo = form.cleaned_data['sexo']
            email = form.cleaned_data['email']

            messages.success(request, 'Cadastro realizado com sucesso')
            form = ClienteForm()
        else:
            messages.error(request, 'Erro ao cadastrar as informações')

    context = {
        'form': form
    }

    return render(request, 'new_cliente.html', context)
    """







