# Etapas de Solução de Problemas

1. Verifique a Instalação e Status do Serviço PostgreSQL:

Confirme se o PostgreSQL está instalado: `dpkg -l postgresql` (ou `apt list --installed postgresql` para versões mais recentes do Ubuntu).
Caso não esteja instalado, instale-o: `sudo apt install postgresql postgresql-contrib`
Inicie o serviço PostgreSQL: `sudo systemctl start postgresql`
Verifique o status do serviço: `sudo systemctl status postgresql` (certifique-se de que esteja em execução) 2. Crie o Banco de Dados:

Conecte-se ao servidor PostgreSQL como usuário com privilégios de superusuário (geralmente "postgres"):

**Entrar no postgres**

- `sudo su - postgres`

**Criar uma tabela**

- `createdb overweb_db`

**Sair do postgres**

- `exit`
