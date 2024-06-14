<div align="center">

 <img height="130" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original-wordmark.svg" />

</div>

# </> | Criando Uma API Com FastAPI Utilizando TDD

- [Repositório do desafio](https://github.com/digitalinnovationone/store_api)

## Criando ambiente virtual

```bash
pyenv virtualenv <python version> <virtual env name>
```

## Excluir ambiente virtual

```bash
pyenv uninstall <virtual env>
```

## Ativando o ambiente virtual e Poetry

```bash
pyenv activate <virtual env name>
```

> **Atualizando o poetry e instalando os pacotes**

```bash
python -m pip install --upgrade pip
```

> **Gerar um arquivo com os pacotes instalados**
```bash
pip freeze > requirements.txt
```

```bash
poetry init
```

**Dependencias instaladas**
```bash
fastapi
uvicorn
pydantic
pydantic-settings
motor
pytest
pytest-asyncio
pre-commit
```

```bash
poetry install
```

## Makefile

```bash
run:
	@uvicorn store.main:app --reload

precommit-install:
	@poetry run pre-commit install

test:
	@poetry run pytest

test-matching:
	@poetry run pytest -s -rx -k $(K) --pdb store ./tests/
```

## Docker Compose

```bash
curl -SL https://github.com/docker/compose/releases/download/v2.27.1/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
```

**Dar permissões de execução**

```bash
chmod +x ~/.docker/cli-plugins/docker-compose
```

**Verificar a instalação** - Para ter certeza que tudo deu certo basta entrar com o comando docker compose version.

```bash
docker compose version
```

Output `docker compose version`:

```bash
Docker Compose version v2.27.1
```

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
sudo docker run hello-world
```

Output `sudo docker run hello-world`:
```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

</details>

## Configurando o Docker Compose File


`docker-compose.yml`
```yml
services:
  db:
    image: 'zcube/bitnami-compat-mongodb'
    ports:
      - 27017:27017
    restart: on-failure
    environment:
      - MONGODB_ADVERTISED_HOSTNAME=localhost
      - ALLOW_EMPTY_PASSWORD=yes
```

```bash
docker compose up -d
```
