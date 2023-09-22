"""
Modulo de funççoes uteis para a aplicação

"""

from datetime import datetime, date
from conversor.models import Cotacao

def converter_dados_de_contacao(reposta_contacao: dict) -> list:
    """Converte os dados da api para objeto contacao

    Args:
        reposta_contacao (dict): Resposta da api de contação 

    Returns:
        list: lista com objeto contação
    """

    data = reposta_contacao.get("date")
    moeda_base = reposta_contacao.get("base")


    return [
        Cotacao(
            data=data,
            moeda=moeda,
            moeda_base=moeda_base,
            cotacao=valor
        )
        for moeda, valor in reposta_contacao.get("rates").items()
    ]

def converter_data(data: str) -> date:
    """
    Converte a string para em tipo date

    Args:
        data (str): string no formato yyyy-mm-dd

    Returns:
        date: string convertida no tipo data
    """
    return datetime.strptime(data, "%Y-%m-%d").date()
