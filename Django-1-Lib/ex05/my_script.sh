#!/bin/sh

VENV_NAME='django_venv'

if [ ! -d "$VENV_NAME" ]; then
    python -m venv "$VENV_NAME"
fi
if [ -f "$VENV_NAME/Scripts/activate" ]; then
    ACTIVATE_FILE="$VENV_NAME/Scripts/activate"
else
    ACTIVATE_FILE="$VENV_NAME/bin/activate"
fi

. "$ACTIVATE_FILE"
pip install -r requirement.txt

exec bash --rcfile <(echo ". ~/.bashrc; . $ACTIVATE_FILE")
