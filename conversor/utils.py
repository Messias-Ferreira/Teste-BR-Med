"""
Modulo de funççoes uteis para a aplicação

"""


from conversor.models import Cotacao
from datetime import datetime, date

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

            
def converter_data(data: date) -> date:

    return datetime.strptime(data, "%Y-%m-%d").date()