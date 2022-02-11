# Docker flask-restx

## Tecnologias utilizadas

- Flask restx
- Uwsgi
- Docker compose
- Postgres
- Nginx

## Instalação

```bash
# Criar ambiente virtual
$ python -m venv .venv

# Ativar ambiente virtual
$ .venv/Scripts/activate

# Instalar dependências
$ pip install -r api/requirements.txt
```

Configurar arquivo .env seguindo o arquivo .env.example

## Iniciar

```bash
$ python start.py
```

## License

[MIT](https://api.github.com/licenses/mit)
