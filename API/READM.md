# </> | Desenvolvendo sua Primeira API com FastAPI, Python e Docker

- [Repositório da aula](https://github.com/digitalinnovationone/workout_api/tree/main/workout_api)

## Criando ambiente virtual

```bash
pyenv virtualenv <python version> <virtual env name>
```

## Ativando o ambiente virtual

```bash
pyenv activate <virtual env name>
```

# Atualizando o pip e instalando os pacotes

```bash
python -m pip install --upgrade pip
```

```bash
pip install fastapi uvicorn sqlalchemy pydantic alembic
```

> **pip list**

```bash
Package           Version
----------------- --------
alembic           1.13.1
annotated-types   0.7.0
anyio             4.4.0
certifi           2024.6.2
click             8.1.7
dnspython         2.6.1
email_validator   2.1.1
exceptiongroup    1.2.1
fastapi           0.111.0
fastapi-cli       0.0.4
greenlet          3.0.3
h11               0.14.0
httpcore          1.0.5
httptools         0.6.1
httpx             0.27.0
idna              3.7
Jinja2            3.1.4
Mako              1.3.5
markdown-it-py    3.0.0
MarkupSafe        2.1.5
mdurl             0.1.2
orjson            3.10.3
pip               24.0
pydantic          2.7.3
pydantic_core     2.18.4
Pygments          2.18.0
python-dotenv     1.0.1
python-multipart  0.0.9
PyYAML            6.0.1
rich              13.7.1
setuptools        65.5.0
shellingham       1.5.4
sniffio           1.3.1
SQLAlchemy        2.0.30
starlette         0.37.2
typer             0.12.3
typing_extensions 4.12.1
ujson             5.10.0
uvicorn           0.30.1
uvloop            0.19.0
watchfiles        0.22.0
websockets        12.0
```

## Ativando o uvicorn

```bash
uvicorn workout_api.main:app --reload
```

> **Makefile**

```bash
run:
	@uvicorn workout_api.main:app --reload
```

> **Makefile _run_**

```bash
make run
```

---

# Docker

## Instalando o Docker

> **1° Passo**

```bash
sudo apt-get update
```

> **2° Passo**
```bash
sudo apt-get install ca-certificates curl gnupg lsb-release
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

> **3° Passo**

```bash
sudo apt-get update
```

<details>

<summary><b>[! - ! - !] Outra Alternativa</b></summary>

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt update
```

```bash
apt-cache policy docker-ce
```

Output of `apt-cache policy docker-ce`:
```bash

docker-ce:
  Installed: (none)
  Candidate: 5:19.03.9~3-0~ubuntu-focal
  Version table:
     5:19.03.9~3-0~ubuntu-focal 500
        500 https://download.docker.com/linux/ubuntu focal/stable amd64 Packages

```

```bash
sudo apt install docker-ce
```

```bash
sudo systemctl status docker
```

Output `sudo systemctl status docker`:
```bash
Output
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2020-05-19 17:00:41 UTC; 17s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 24321 (dockerd)
      Tasks: 8
     Memory: 46.4M
     CGroup: /system.slice/docker.service
             └─24321 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
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
    image: postgres:11-alpine
    environment:
      POSTGRES_PASSWORD: workout
      POSTGRES_USER: workout
      POSTGRES_DB: workout
    ports:
      - "5432:5432"
```

```bash
docker compose up -d
```