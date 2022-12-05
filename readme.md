# Resumo sobre a API:
Para obter os resultados desejados você tera que utilizar ferramentas como o [Postman](https://www.postman.com/) ou o [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)  para o consumo dessa API.
- Qualquer coisa o projeto também estará no replit: [@LucasSantos122](https://replit.com/@LucasSantos122/NewFlask#main.py)

# Rotas
As rotas foram definidas de maneira simples, foi utilizado o Replit para desenvolver a API, a partir daqui irei citar as rotas junto a seus métodos de requisição, para que seja possível trabalhar com elas:

* NewFlask.lucassantos122.repl.co`/listar` METHOD = [GET]
	>Traz a lista de **TODOS** os cadastros, em formato de `JSON` seguindo o padrão REST 

* NewFlask.lucassantos122.repl.co`/cadastrar` METHOD = [POST]
	>Realiza um cadastro a partir do envio de um JSOM com o corpo:
	`{"nome":"FIRST_NAME", "sobrenome":"SECOND_NAME",
	"cpf":"CPF", "rg":"RG", "data_nasc":"DD/MM/YYYY"}`.

* NewFlask.lucassantos122.repl.co`/pesquisar/<ID_PEOPLE>` METHOD = [GET]
	>Algumas rotas possuem parâmetros que devem ser passados pelo próprio corpo para realizarem certas funções,  a rota `/pesquisar`, por exemplo, precisa de um parâmetro numérico(inteiro) para encontrar o **ID** ficando, por exemplo: `pesquisar/1200` .

* NewFlask.lucassantos122.repl.co`/atualizar` METHOD = [PUT]
	>A rota `/atualizar` utiliza a comunicação por JSON assim como a rota de cadastro, seu corpo: 
	`{"id": "ID_USER", "nome":"FIRST_NAME", "sobrenome":"SECOND_NAME", "cpf":"CPF", "rg":"RG", "data_nasc":"DD/MM/YYYY"}` o ID do usuário também poderia ser passado pelo corpo da rota.

* NewFlask.lucassantos122.repl.co`/deletar/<ID_PEOPLE>`  METHOD = [DELETE]
	>A rota `/deletar/<ID_PEOPLE>` também precisa de um **ID** valido passado em seu corpo. Para realizar a ação de deletar.

# Sobre a organização dos arquivos:
O projeto foi pensado de maneira modular para ser de fácil manutenção deis do banco até suas funções para as rotas.	Dividindo sua estrutura em dois arquivos principais (sem contar o banco) sendo:
* `main.py`
* `functions.py`
	
Com `main.py` sendo o aquivo principal para as rotas que acabam chamando as funções do arquivo `function.py` e que se conectam através da função `get_database()`.

----
|Programadores|
|--------------------|
|Lucas Santos Campos|
|Eddie Mauricio Silva dos Santos|
|Rodrigo Ferreira Pereira|
|Sergio Lima Borges|
|Yuri Mathaus Cavalcante Ferreira|
|Nathalia Daniel da Silva|

-----
-----
-----
# Summary about the API:
To get the desired results you will have to use tools like [Postman](https://www.postman.com/) or [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav. vscode-thunder-client) for consuming this API.
- Anything the project will also be in the replit: [@LucasSantos122](https://replit.com/@LucasSantos122/NewFlask#main.py)

# routes
The routes were defined in a simple way, Replit was used to develop the API, from here I will quote the routes along with their request methods, so that it is possible to work with them:

* NewFlask.lucassantos122.repl.co`/listar` METHOD = [GET]
>Brings the list of **ALL** entries, in `JSON` format following the REST pattern

* NewFlask.lucassantos122.repl.co`/cadastrar` METHOD = [POST]
>Register by sending a JSOM with the body:
`{"firstname":"FIRST_NAME", "lastname":"SECOND_NAME",
"cpf":"CPF", "rg":"RG", "date_birth":"DD/MM/YYYY"}`.

* NewFlask.lucassantos122.repl.co`/pesquisar/<ID_PEOPLE>` METHOD = [GET]
>Some routes have parameters that must be passed by the body itself to carry out certain functions, the `/search` route, for example, needs a numeric parameter (integer) to find the **ID**, for example: `search /1200` .

* NewFlask.lucassantos122.repl.co`/atualizar` METHOD = [PUT]
>The `/update` route uses JSON communication as well as the registration route, its body:
`{"id": "ID_USER", "name":"FIRST_NAME", "last name":"SECOND_NAME", "cpf":"CPF", "rg":"RG", "birth_date":"DD/MM /YYYY"}` The userid could also be passed in the route body.

* NewFlask.lucassantos122.repl.co`/deletar/<ID_PEOPLE>` METHOD = [DELETE]
>The `/delete/<ID_PEOPLE>` route also needs a valid **ID** passed in its body. To perform the delete action.

# About the organization of the files:
The project was designed in a modular way to be easy to maintain from the bank to its functions for the routes. Dividing its structure into two main files (not counting the bank) being:
* `main.py`
* `functions.py`

With `main.py` being the main file for the routes that end up calling the functions in the `function.py` file and connecting via the `get_database()` function.


|🇧🇷 Programmers 🇧🇷 |
|--------|
| Lucas Santos Campos |
|Eddie Mauricio Silva dos Santos|
|Rodrigo Ferreira Pereira|
|Sergio Lima Borges|
| Yuri Mathhaus Cavalcante Ferreira |
|Nathalia Daniel da Silva|
