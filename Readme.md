## Passos do projeto

### Criar e ativar ambiente virtual
- ```sh
    python3 -m venv .venv

- linux: diretorio/bin/activate
- windows: diretorio\Scripts\Activate

### Atualizar e/ou instalar pip dentro do ambiente virtual

- ```sh
    & "local_diretorio\.venv\Scripts\python.exe" -m pip install --upgrade pip

ou

- ```sh
    python.exe -m pip install --upgrade pip

### Caso seja feito git clone, este comando instala todos os pacotes listados dentro de requirement.txt:
- ```sh
    pip install -r requirements.txt

### Caso seja projeto novo, instalar todos os pacotes necessários para o projeto
- ```sh
    pip install black

- ```sh
    pip install flake8

- ativar eslint com ctrl+shift+p -> "Select linter" -> flake8

- ```sh
    pip install python-dotenv

- ```sh
    pip install cx_Oracle

### Criar arquivo replicador de ambiente
- ```sh
    pip freeze > requirements.txt

## OBS: É preciso recuperar o .env com as variáveis de ambiente, baixar o arquivo de instantclient e atualizar dentro do .env a direção do mesmo.

#### Referencias
> - https://www.alura.com.br/artigos/ambientes-virtuais-em-python?gclid=Cj0KCQiA4aacBhCUARIsAI55maHQdV2kmyuY0e0i4FpGz5MHGzhXyLPjV_UyHliR_3_GZSSz1RvGfdYaArHcEALw_wcB
> - https://gist.github.com/leocomelli/2545add34e4fec21ec16
> - https://docs.oracle.com/pt-br/iaas/autonomous-database-shared/doc/connecting-python-tls.html#GUID-408A6DE2-6C3A-4159-86DB-DE1AFCBE4E80
> - https://cx-oracle.readthedocs.io/en/latest/user_guide/connection_handling.html#net-service-names-for-connection-strings
