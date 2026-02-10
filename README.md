# Agenda em Python usando Flask

Este Projeto foi elaborado por Cauãzito, para permitir o aprendizado de conecitos como o padrão de projeto MVC (Model-View-Controller), framework Flask e seus componentes, variáveis de ambiente, paradigma de programação orientado a objetos e reforço de fundamentos da linguagem de programção Python.

Para implementar este projeto localmente, siga os seguintes passos:

1. Faça fork deste repositório, clicando no botão `Fork`

2. Clone seu repositório localmente:

~~~bash
git clone <url_repositorio>
~~~

3. Abra o projeto utilizando seu IDE preferido


4. Crie, preferencialmente, um ambiente virtual utilizando sua versão do Python >3.12.10


~~~bash 
python -m venv .venv
~~~

5. Ative seu ambiente virtual.
        
        No bash:

        ~~~bashsource .venv/Scripts/activate
        ~~~ 

        No PowerShell:
        ~~~powershell
        .venv\Scripts\Activate.ps1
        ~~~

    6. Instale todas as dependências constantes no arquivo `requeriments.txt`;
    ~~python
    pip install -r requeriments.txt

    7. Copie o arquivo `.env.example`, cole na raiz do projeto e renomeie a copia para .env example

    8. Edite o arquivo `.env` para defenir o caminho do seu banco de dados, na constante `DATABASE`

    9. Rode a aplicação no Python utilizando o comando:
    
    ~~~bash
    flask run
    ~~~

    10. Acesse a aplicação no endereço de porta indicados no terminal. Exemplo:
    `https://127.0.0.1:5000`