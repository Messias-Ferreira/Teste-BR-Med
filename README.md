# Sistema de Contação - Teste para BR-Med :rocket:

Este é um sistema de contação desenvolvido como parte de um teste para a BR-Med, utilizando Python 3.10. O sistema permite a contação de itens e inclui funcionalidades para rodar o projeto localmente, popular a base de dados e executar testes locais.

## Pré-requisitos

- Python 3.10 (ou uma versão compatível)
- Docker
- Docker Compose


## 1. Rodando o Projeto Localmente

Para rodar o projeto localmente usando Docker Compose, siga os passos abaixo:

1. Clone o repositório do projeto para o seu ambiente de desenvolvimento.

2. ADD na raiz do projeto o .env com os paramentros informado no email

~~~shell
   git clone https://github.com/Messias-Ferreira/Teste-BR-Med.git
   cd Teste-BR-Med
~~~
3. Execute o seguinte comando para rodar o projeto localmente com Docker Compose:
~~~shell
    make local
~~~
4. O sistema estará disponível em http://localhost:8000 no seu navegador.


## 2. Populando a Base de Dados

Para popular a base de dados com itens de teste, siga os passos abaixo:

1. Certifique-se de que o projeto está rodando localmente (veja as instruções acima).

2. Execute o seguinte comando para popular a base de dados:

~~~shell
    make popular_base
~~~
3. A base de dados agora estará preenchida com dados de teste.

## 3. Executando Testes Locais

Para executar os testes locais, siga os passos abaixo:

1. Certifique-se de que o projeto está rodando localmente (veja as instruções acima).

2. Execute o seguinte comando para executar os testes locais:
~~~shell
    make testes
~~~
3. Os testes serão executados, e os resultados serão exibidos no terminal.