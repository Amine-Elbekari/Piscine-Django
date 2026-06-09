#!/bin/bash
set -e

VENV_NAME='django_final'

if [ ! -d "$VENV_NAME" ]; then
    python -m venv "$VENV_NAME"
fi
if [ -f "$VENV_NAME/Scripts/activate" ]; then
    ACTIVATE_FILE="$VENV_NAME/Scripts/activate"
else
    ACTIVATE_FILE="$VENV_NAME/bin/activate"
fi

source "$ACTIVATE_FILE"

pip install django
pip install psycopg2
pip install django-environ
pip install django-extensions
pip install pytest
pip install djangorestframework
pip install markdown
pip install django-filter
pip install pillow

pip freeze > requirements.txt

exec bash --rcfile <(echo ". ~/.bashrc; . $ACTIVATE_FILE")