## Configurando

Quando você baixar o projeto, é necessário ter uma virtualenv criada. Você pode fazer isso usando `poetry`, `pipenv` ou até mesmo o `pip`. Mas neste exemplo iremos utilizar o pip, e por que usar o pip? Porque ele já vem com o python.

Rode:

`python -m venv .venv`

E rode o source para ativar a .env

`source .venv/bin/activate`

## Instalando dependências

Para instalar todas as dependências você precisa rodar o comando abaixo:

`pip install -r requirements.txt`

Agora, você pode rodar a aplicação utilizando o comando `flask run`, mas note, que é necessário que o mongodb esteja rodando em background. Se você não tem o mongo instalado, pode fazer isso utilizando o docker.


