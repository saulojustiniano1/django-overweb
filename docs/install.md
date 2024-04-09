# Como instalar o Django

- Veriﬁque se o Python está instalado: `python --version`
- **(Opcional)** Crie um ambiente virtual: `python -m venv venv` _(Isso criará um ambiente virtual
  chamado "venv")_
- Ative o ambiente virtual: No Windows: `.\venv\Scripts\activate` No Mac/Linux: `source -m venv/bin/activate`
- Instale o Django (Com o ambiente virtual ativado): `pip install django`
- Veriﬁque a instalação: `django-admin --version`

# Como criar um projeto Django

- Crie um projeto Django: `django-admin startproject nome_projeto`
- Entre no diretório do projeto: `cd nome_projeto`
- Execute o servidor de desenvolvimento: `python manage.py runserver`
- Acesse o projeto no navegador: `http://localhost:8000`

# Como criar uma aplicação Django

- Crie uma aplicação Django: `python manage.py startapp nome_app`
- Adicione a aplicação ao projeto: Adicione o nome da aplicação no arquivo `settings.py`
- Crie um modelo: Crie uma classe no arquivo `models.py`
- Execute as migrações: `python manage.py makemigrations` e `python manage.py migrate`
- Crie um superusuário: `python manage.py createsuperuser`
- Execute o servidor de desenvolvimento: `python manage.py runserver`
- Acesse a aplicação no navegador: `http://localhost:8000`

# Como resolver o erro "Port is already in use"

Uma solução mais simples, basta digitar **sudo fuser -k 8000/tcp**.
Isso deve matar todos os processos associados à porta 8000.

### Como criar um arquivo requirements.txt em um projeto Django

Para criar um arquivo `requirements.txt` em um projeto Django, você precisa seguir os seguintes passos:

1. Abra o terminal na raiz do seu projeto Django.
2. Ative o ambiente virtual do seu projeto, se você estiver usando um.
3. Execute o comando `pip freeze > requirements.txt`.

Este comando irá gerar um arquivo `requirements.txt` na raiz do seu projeto, que lista todas as bibliotecas Python instaladas no ambiente virtual atual, juntamente com suas versões. Isso é útil para garantir que todos que trabalham no projeto tenham as mesmas versões das bibliotecas.

Aqui está o pseudocódigo:

```plaintext
# Pseudocódigo
1. Abrir o terminal
2. Navegar até a raiz do projeto Django
3. Se estiver usando um ambiente virtual, ativá-lo
4. Executar o comando `pip freeze > requirements.txt`
```

E aqui está o comando de terminal correspondente:

```bash
pip freeze > requirements.txt
```

Lembre-se de que este comando deve ser executado no ambiente virtual onde o Django e outras dependências do projeto estão instaladas.
