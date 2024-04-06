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
