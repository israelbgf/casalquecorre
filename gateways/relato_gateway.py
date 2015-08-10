import re
from core.entities.relato import Relato

class RelatoGatewayArquivoTXT(object):

    TITULO = 0
    BIANCA = 1
    ISRAEL = 2

    def __init__(self, arquivo):
        self.arquivo = arquivo

    def listar(self):

        relatos = []
        regiao = None
        for linha in self.arquivo:
            linha = linha.strip()

            if linha.startswith('--'):
                regiao = self.TITULO
                continue
            elif not linha:
                continue

            if regiao == self.TITULO:
                relato = Relato()
                grupos = re.match('(.*)-(.*)\{(.*)}', linha).groups()
                relato.data, relato.titulo, relato.nome_foto = map(lambda item: item.strip(), grupos)
                regiao = self.BIANCA
            elif regiao == self.BIANCA:
                relato.texto_bianca = linha
                regiao = self.ISRAEL
            elif regiao == self.ISRAEL:
                relato.texto_israel = linha
                relatos.append(relato)
                regiao = None

        return relatos
