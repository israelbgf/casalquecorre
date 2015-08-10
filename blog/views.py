from django.http import HttpResponse
from django.shortcuts import render
from gateways.relato_gateway import RelatoGatewayArquivoTXT


def index(request):
    gateway = RelatoGatewayArquivoTXT(open('relatos/relatos.html'))
    relatos = gateway.listar()

    return render(request, 'blog/index.html', {
        'relatos': relatos
    })
