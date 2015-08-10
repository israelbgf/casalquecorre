# coding=utf-8
from unittest.case import TestCase
from StringIO import StringIO

from hamcrest.core import assert_that
from hamcrest.core.core.is_ import is_
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection.is_empty import empty
from hamcrest.library.object.haslength import has_length
from gateways.relato_gateway import RelatoGatewayArquivoTXT

TITULO = 'Joinville: Treino no Batalhão'
DATA = '30 de Julho de 2015'
NOME_FOTO = '20150730.png'
TEXTO_BIANCA = 'Texto bianca.'
TEXTO_ISRAEL = 'Texto israel.'


class QuandoNaoExistemRelatos(TestCase):

    def setUp(self):
        self.gateway = RelatoGatewayArquivoTXT(StringIO())

    def test_retorna_vazio(self):
        relatos = self.gateway.listar()
        assert_that(relatos, is_(empty()))

class QuandoExisteUmRelato(TestCase):

    def setUp(self):
        arquivo = StringIO('''
---------------------------------------------
30 de Julho de 2015 - Joinville: Treino no Batalhão {20150730.png}

Texto bianca.

Texto israel.
        ''')
        self.gateway = RelatoGatewayArquivoTXT(arquivo)

    def test_retorna_um_relato(self):
        relatos = self.gateway.listar()

        assert_that(relatos, has_length(1))

        assert_that(relatos[0].titulo, equal_to(TITULO))
        assert_that(relatos[0].data, equal_to(DATA))
        assert_that(relatos[0].nome_foto, equal_to(NOME_FOTO))
        assert_that(relatos[0].texto_bianca, equal_to(TEXTO_BIANCA))
        assert_that(relatos[0].texto_israel, equal_to(TEXTO_ISRAEL))

class QuandoExistemDoisOuMaisRelatos(TestCase):

    def setUp(self):
        arquivo = StringIO('''
---------------------------------------------
25 de Julho de 2015 - Tubarao: Treino no Batalhão {20150730.png}

Texto bianca diferente.

Texto israel diferente.
---------------------------------------------
30 de Julho de 2015 - Joinville: Treino no Batalhão {20150730.png}

Texto bianca.

Texto israel.
        ''')
        self.gateway = RelatoGatewayArquivoTXT(arquivo)

    def test_retorna_dois_relatos(self):
        relatos = self.gateway.listar()

        assert_that(relatos, has_length(2))

        assert_that(relatos[1].titulo, equal_to(TITULO))
        assert_that(relatos[1].data, equal_to(DATA))
        assert_that(relatos[1].nome_foto, equal_to(NOME_FOTO))
        assert_that(relatos[1].texto_bianca, equal_to(TEXTO_BIANCA))
        assert_that(relatos[1].texto_israel, equal_to(TEXTO_ISRAEL))
