# Readbook

Bem-vindo ao **Readbook**, a plataforma web de cadastro de livros! Este README fornecerá uma visão geral do projeto, instruções sobre como configurá-lo e como utilizá-lo. Vamos começar!

## Descrição do Projeto

**Readbook** é um site de cadastro de livros desenvolvido com Django. O projeto permite que usuários se cadastrem, façam login e gerenciem seus livros favoritos. Abaixo, detalhamos as principais funcionalidades e passos para configurar o ambiente de desenvolvimento.

## Funcionalidades

- **Autenticação de Usuário**: Tela de login e cadastro de novos usuários (sign-up).
- **Cadastro de Livros**: Usuários autenticados podem adicionar novos livros ao seu acervo.
- **Visualização de Livros**: Usuários podem visualizar a lista de livros cadastrados.

## Tecnologias Utilizadas

- **Framework**: Django
- **Linguagem**: Python
- **Banco de Dados**: PostgreSQL
- **Frontend**: Bootstrap

## Configuração do Ambiente de Desenvolvimento

Siga os passos abaixo para configurar o projeto em sua máquina local:

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/JeffersonGuedes/Plataforma_web.git
    cd Plataforma_web
    ```

2. **Crie um ambiente virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados**:
    Atualize as configurações do banco de dados em `settings.py` para conectar ao PostgreSQL.

5. **Realize as migrações do banco de dados**:
    ```bash
    python manage.py migrate
    ```

6. **Execute o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

7. **Acesse a aplicação**:
    Abra o navegador e acesse `http://127.0.0.1:8000/`.

## Como Usar

1. **Tela de Login/Cadastro**: Ao acessar o site, você será redirecionado para a tela de login. Caso não tenha uma conta, clique em "Sign Up" para se cadastrar.
2. **Cadastrar Livros**: Após fazer login, você poderá acessar a página de cadastro de livros, onde poderá adicionar novos livros ao seu acervo.
3. **Visualizar Livros**: Na página principal, você verá uma lista com todos os livros cadastrados.

## Estrutura do Projeto

- `core/`: Contém os arquivos de configuração do projeto Django.
- `home/`: Aplicação Django responsável pelo gerenciamento dos livros.
- `templates/`: Arquivos HTML para as páginas do site.
- `static/`: Arquivos estáticos (CSS, JavaScript, imagens).
- `manage.py`: Script de gerenciamento do Django.

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou encontrar algum bug, sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

Esperamos que você aproveite a experiência de usar o **Readbook**! Se tiver alguma dúvida ou precisar de assistência, não hesite em entrar em contato.

Boas leituras!
