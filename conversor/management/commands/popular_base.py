"""
Modulo para popular a base
"""
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError

from conversor.models import Cotacao
from conversor.api.vatcomply import VatComply
from conversor.utils import converter_dados_de_contacao


class Command(BaseCommand):
    """
    Comando para popular a base
    """

    help = "Popula a base de acordo com os dias informados"

    def add_arguments(self, parser):
        parser.add_argument("dias", type=int)

    def handle(self, *args, **options):
        try:
            datas = [
                datetime.now() - timedelta(days=_)
                for _ in range(1, options["dias"])
            ]

            cotacoes = [
                converter_dados_de_contacao(
                    VatComply.get_contacao_por_data(data)
                )
                for data in datas
            ]

            for contacoes_dia in cotacoes:
                Cotacao.objects.bulk_create(contacoes_dia)

        except Exception as e:
            raise CommandError(f"Erro ao popular a base: {e}")

        self.stdout.write(
            self.style.SUCCESS("Base populada com sucesso")
        )
