# Projeto-PGP

## Configurar Ambiente

Primeiro, crie um arquivo .env com base no .env-example, lembrando de
trocar o DEBUG para 1. Depois rode os comandos, um por vez:

    python -m venv venv

    source venv/bin/activate

    pip install -r requirements.txt

    python manage.py migrate
    
    python manage.py createsuperuser

    python manage.py runserver

