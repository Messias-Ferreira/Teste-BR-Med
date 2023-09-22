"""
Modulo de testes dos projeto.

Obs. Os testes foram criados no mesmo arquivo para facilitação da leitura do avaliador
uma boa pratica seria quebrar cada modulo em diferentes modulos teste
"""

from datetime import datetime, date

from django.test import TestCase, Client
from rest_framework.test import APIClient

from conversor.api.vatcomply import VatComply
from conversor.utils import converter_data, converter_dados_de_contacao
from conversor.models import Cotacao


class CotacaoTests(TestCase):
    """
    Classe de teste do app conversor
    """
    def setUp(self) -> None:
        self.data = datetime.strptime("20/09/2023", "%d/%m/%Y")
        self.client = Client()
        self.cliente_api = APIClient()

    def test_api_vatcomply(self):
        """
        Testa a conexão com o serviço da vatcomply
        """
        resposta = VatComply.get_contacao_por_data(self.data)

        self.assertTrue(resposta)

    def test_api_vatcomply_resposta(self):
        """
        testa se a reposta da vat comply esta de acordo com o que a gnt esta esperando
        """
        mock_teste = {
            "date": "2023-09-20",
            "base": "USD",
            "rates": {
                "EUR": 0.9344047841524948,
                "USD": 1.0,
                "JPY": 147.89758923565688,
                "BGN": 1.8275088768454493,
                "CZK": 22.788263875911046,
                "DKK": 6.963931975331714,
                "GBP": 0.8085404597271537,
                "HUF": 358.5311156793123,
                "PLN": 4.335918519902822,
                "RON": 4.645486824892543,
                "SEK": 11.101009157166885,
                "CHF": 0.8971220332648102,
                "ISK": 135.7690151373575,
                "NOK": 10.728835731638945,
                "TRY": 27.035974584189873,
                "AUD": 1.541581012894786,
                "BRL": 4.857222948981499,
                "CAD": 1.3423659129134742,
                "CNY": 7.293870304615959,
                "HKD": 7.822743412446272,
                "IDR": 15357.53130256027,
                "ILS": 3.8080732573350775,
                "INR": 83.08007849000187,
                "KRW": 1327.2192113623623,
                "MXN": 17.032984488880583,
                "MYR": 4.68547934965427,
                "NZD": 1.6768828256400672,
                "PHP": 56.7211736124089,
                "SGD": 1.3624556157727528,
                "THB": 36.05961502522893,
                "ZAR": 18.836852924686973,
            },
        }

        resposta = VatComply.get_contacao_por_data(self.data)

        self.assertDictEqual(resposta, mock_teste)

    def test_utils_conversor_data(self):
        """
        testa o conversor da data 
        """
        data = "2023-09-20"

        dt_convertida = converter_data(data)

        self.assertIsInstance(dt_convertida, date)

    def test_utils_normalizador_dados(self):
        """
        Testa a nomalização dos dados vindo vat comply
        """
        mock_teste = {
            "date": "2023-09-20",
            "base": "USD",
            "rates": {
                "EUR": 0.9344047841524948,
                "USD": 1.0,
                "JPY": 147.89758923565688,
                "BGN": 1.8275088768454493,
                "CZK": 22.788263875911046,
                "DKK": 6.963931975331714,
                "GBP": 0.8085404597271537,
                "HUF": 358.5311156793123,
                "PLN": 4.335918519902822,
                "RON": 4.645486824892543,
                "SEK": 11.101009157166885,
                "CHF": 0.8971220332648102,
                "ISK": 135.7690151373575,
                "NOK": 10.728835731638945,
                "TRY": 27.035974584189873,
                "AUD": 1.541581012894786,
                "BRL": 4.857222948981499,
                "CAD": 1.3423659129134742,
                "CNY": 7.293870304615959,
                "HKD": 7.822743412446272,
                "IDR": 15357.53130256027,
                "ILS": 3.8080732573350775,
                "INR": 83.08007849000187,
                "KRW": 1327.2192113623623,
                "MXN": 17.032984488880583,
                "MYR": 4.68547934965427,
                "NZD": 1.6768828256400672,
                "PHP": 56.7211736124089,
                "SGD": 1.3624556157727528,
                "THB": 36.05961502522893,
                "ZAR": 18.836852924686973,
            },
        }

        dados_normalizados = converter_dados_de_contacao(mock_teste)

        self.assertIsInstance(dados_normalizados, list)

        for dado in dados_normalizados:
            self.assertIsInstance(dado, Cotacao)

        self.assertEqual(len(dados_normalizados), len(mock_teste.get("rates")))

    def test_views_frontend(self):
        """
        testa o frontend
        """
        resposta = self.client.get("/")

        self.assertEqual(200, resposta.status_code)
        self.assertContains(resposta, "Bem Vindo ao sistema de cotação")
        self.assertTemplateUsed(resposta, "conversor/index.html")

    def test_views_api_cotacao(self):
        """
        testa a api de dados
        """
        resposta = self.cliente_api.get(
            "/consulta",
            {"dt_inicio": "2023-09-04", "dt_fim": "2023-09-06"},
        )
        self.assertEqual(200, resposta.status_code)
