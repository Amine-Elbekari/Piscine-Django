#!/bin/bash

VENV_NAME='django_sessions'

if [ ! -d "$VENV_NAME" ]; then
    python -m venv "$VENV_NAME"
fi
if [ -f "$VENV_NAME/Scripts/activate" ]; then
    ACTIVATE_FILE="$VENV_NAME/Scripts/activate"
else
    ACTIVATE_FILE="$VENV_NAME/bin/activate"
fi

source "$ACTIVATE_FILE"

if [[ -z $(pip freeze) ]]; then
    if [ -f "requirements.txt" ]; then 
        pip install -r requirements.txt
    fi
else
    echo "Dependencies already installed."
fi
exec bash --rcfile <(echo ". ~/.bashrc; . $ACTIVATE_FILE")