from django.shortcuts import render
from gateways.relato_gateway import RelatoGatewayArquivoTXT


def index(request):
    with open('relatos/relatos.html') as arquivo:
        gateway = RelatoGatewayArquivoTXT(arquivo)
        relatos = gateway.listar()

    return render(request, 'blog/index.html', {
        'relatos': relatos
    })
