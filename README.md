# OPEN FOOD FACTS API

API para consulta de alimentos e suas propriedades para fins nutricionais. Baseado no PythonChallenge

## Instruções/Pré-Requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Python](https://www.python.org/) e [Docker](https://www.docker.com).
Além disto é bom ter um editor para trabalhar com o código como o [VSCode](https://code.visualstudio.com/) ou [Pycharm](https://www.jetbrains.com/pt-br/pycharm/)

## Rodando o servidor Backend
```bash

# Clonar o repositório
$ git clone <https://lab.coodesh.com/daniel_santana_oliveira/python-challenge-20200205.git>

# Abra o projeto na sua IDE
# Instale as dependências pip install -r requirements
# Crie o arquivo .env seguindo como base o .env_example
# Adicione os enviroments JWT_SECRET_KEY=(qualquer valor) MONGO_ROOT_USERNAME('adm')  MONGO_ROOT_PASSWORD('12345')
# No terminal execute o comando docker compose up-d
# Esse comando ira criar um container do servidor e do bando de dados MongoDB
# O servidor iniciará na porta 3000
# Fazer uma requisição para o endpoint(`/register`) passando no body [username,password] para a criação de um usuário
# Se autenticar fazendo uma requisição para (`/login`) passando no body [username,password], gerando um access_token
# Para consultar as demais rotas deve se passar o bearer token no header da requisição

```


## Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/) , linguagem de programação
- [Docker](https://www.docker.com), ambiente de desenvolvimento para criar containers
- [Flask](https://flask.palletsprojects.com/en/3.0.x/), um microframework para desenvolvimento webem Python
- [MongoDB](https://www.mongodb.com/pt-br), é um banco de dados não-relacional orientado a documentos
- [JSON web token](https://jwt.io/), padrão de autenticação e geração de tokens

## Endpoints

 - `GET /`: Detalhes da API, se conexão leitura e escritura com a base de dados está OK, tempo online do servidor
 - `PUT /products/:code`: responsável por atualizar as informações do alimento
 - `DELETE /products/:code`: Muda o status do produto para `trash`
 - `GET /products/:code`: Obtém informações de um determindado produto
 - `GET /products`: Listar todos os produtos da base de dados
 - `POST /login`: Autenticação no servidor para ter acesso aos endpoints
 - `POST /register`: criação de um usuário

## Licença

Projeto desenvolvido com base nos requisitos pedidos no desafio PythonChallenge.