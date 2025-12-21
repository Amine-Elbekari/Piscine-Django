#!/bin/sh

VENV_NAME='VENV'

if [ ! -d "$VENV_NAME" ]; then
    python -m venv "$VENV_NAME"
fi

read -p "activate or deactivate? " action
if [ "$action" = "activate" ]; then
    . "$VENV_NAME/Scripts/activate"
elif [ "$action" = "deactivate" ]; then
    deactivate
else
    echo 'Error: Invalid arguments'
fi
