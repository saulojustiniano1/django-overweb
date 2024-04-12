# Instalação do psycpg2 no Ubuntu

- `pip install psycopg2-binary`

# Instalação do postgres no Ubuntu

- link: <https://www.youtube.com/watch?v=cdhpmaa4YJE>

# Configurações de porta do PostgreSQL no Django para Ubuntu

Se você encontrar erros de conexão e tiver certeza de que a senha e o nome de usuário estão corretos, você pode solucionar outros problemas potenciais, como:

Verificar se o serviço PostgreSQL está em execução:
-> `sudo systemctl status postgresql`

Se o serviço não estiver em execução, inicie-o com o seguinte comando:
-> `sudo systemctl start postgresql`

Verificar se o firewall está configurado para permitir conexões ao PostgreSQL:
-> `sudo ufw status`

Se o firewall estiver bloqueando a porta 5432, abra a porta com o seguinte comando:
-> `sudo ufw allow 5432`

Ative o firewall e verifique o status:
-> `sudo ufw enable`

Verifique se a porta 5432 está aberta:
-> `sudo ufw status`

Reiniciar o computador:
-> `sudo reboot`
