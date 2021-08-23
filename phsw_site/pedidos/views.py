from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import facade
from django.core.paginator import Paginator

from .models import ItemForm


@login_required
def fazer_pedido(request):
    categoria_queryset = facade.buscar_itens_por_categoria()
    if request.method != 'POST':
        return render(request, 'pedidos/fazer_pedido.html', context={'categorias': categoria_queryset})

    if request.method == 'POST':
        facade.fazer_pedido(request)
        return render(request, 'pedidos/fazer_pedido.html', context={'categorias': categoria_queryset})


@login_required
def ver_pedidos(request):
    pedidos_queryset = facade.buscar_pedidos(request)
    paginator = Paginator(pedidos_queryset, 3)
    page = request.GET.get('page')
    pedidos_paginator = paginator.get_page(page)
    return render(request, 'pedidos/ver_pedidos.html', context={'pedidos': pedidos_paginator})


@login_required
def ver_pedido(request):
    pedido = facade.buscar_pedido(request)
    return render(request, 'pedidos/ver_pedido.html', context={'pedido': pedido})


@login_required
def editar_itens(request):
    messages.error(request, "Erro ao enviar formulario.")
    form = ItemForm()
    if request.method is 'POST':
        facade.editar_itens(request)
    itens = facade.buscar_todos_os_itens_por_categoria()
    return render(request, 'pedidos/editar_itens.html', context={'categorias': itens, 'form': form})


