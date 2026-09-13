# Sistema de Login com Django

Projeto didático de autenticação de usuários usando o sistema nativo do Django.

## Funcionalidades

- Login com usuário e senha
- Senha ocultada no formulário HTML
- Senhas armazenadas com hash pelo Django
- Controle de sessão
- Logout
- Página protegida com `login_required`
- Redirecionamento após login e logout
- Banco de dados SQLite para desenvolvimento

## Requisitos

- Python 3.10 ou superior
- pip
- Git

## Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO
```

Crie e ative um ambiente virtual.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale o Django:

```bash
pip install django
```

Aplique as migrações:

```bash
python manage.py migrate
```

Crie um usuário administrador para teste:

```bash
python manage.py createsuperuser
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/login/
```

O painel administrativo fica em:

```text
http://127.0.0.1:8000/admin/
```

## Estrutura do projeto

```text
projeto/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── contas/
│   ├── migrations/
│   ├── templates/
│   │   └── contas/
│   │       ├── login.html
│   │       └── painel.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
└── requirements.txt
```

## Rotas principais

| Rota | Função |
|---|---|
| `/login/` | Exibe e processa o formulário de login |
| `/logout/` | Encerra a sessão do usuário |
| `/painel/` | Exibe a página protegida |
| `/admin/` | Acessa o painel administrativo do Django |

## Comandos úteis

Criar uma nova aplicação:

```bash
python manage.py startapp nome_da_app
```

Verificar problemas no projeto:

```bash
python manage.py check
```

Criar migrações após alterar modelos:

```bash
python manage.py makemigrations
python manage.py migrate
```

Gerar dependências instaladas:

```bash
pip freeze > requirements.txt
```

## Segurança

Este projeto é educacional. Antes de publicar em produção:

- altere `SECRET_KEY` e mantenha-a fora do repositório;
- configure `DEBUG = False`;
- defina corretamente `ALLOWED_HOSTS`;
- use HTTPS;
- não publique senhas, tokens ou arquivos `.env`;
- configure banco de dados e variáveis de ambiente para produção.

## Licença

Este projeto pode ser utilizado para fins de estudo.
