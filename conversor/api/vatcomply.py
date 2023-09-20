"""
Modulo api de busca os dados para conversão

"""
from main.settings import URL_HOST
from datetime import datetime

import requests


class VatComply:
    """
    Classe de integração com api
    """

    __URL_HOST: str = URL_HOST


    @classmethod
    def get_contacao_por_data(cls, data: datetime) -> dict:
        """
        Retorna as contação do dola co

        Args:
            data (datetime): _description_

        Raises:
            Exception: _description_

        Returns:
            dict: _description_
        """        

        resposta = requests.get(
            cls.__URL_HOST + f"/rates?base=USD&date={data.strftime('%Y-%m-%d')}",
            timeout=60
        )

        if not resposta.ok:
            raise Exception("Erro ao consultar API da VatComply")
        
        return resposta.json()