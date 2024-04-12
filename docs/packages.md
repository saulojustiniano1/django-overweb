# Configurando Virtual Environments

Caso você não tenha o virtual environments instalado este tutorial deve lhe ajudar. Para criar virtual environments em seu projeto e criar corretamente o arquivo requirements.txt você pode seguir os seguintes passos:

- Navegar até o diretório raiz da sua aplicação python pelo terminal e digitar `python -m venv venv`. Caso tenha varias versões do python em sua máquina e queira usar alguma versão especifica também é possível, ex: `python3.6 -m venv venv` .
- Ativar venv no windows digite no terminal `.\venv\Scripts\activate.bat` , no linux `source <venv>/bin/activate`
- Instalar os pacotes necessários `pip install <pacote>`
- Gerar o requirements.txt `pip freeze > requirements.txt`

Pronto, agora seu arquivo requirements.txt conterá somente as dependências necessárias para rodar o seu projeto.

# Instalando pacotes requirements.txt

Quando for necessário instalar os pacotes registrados no requirements.txt você pode digitar o seguinte comando no terminal.

`pip install -r requirements.txt`
