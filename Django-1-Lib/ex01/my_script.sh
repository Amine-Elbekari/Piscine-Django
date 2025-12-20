#!/bin/sh

pip install --force-reinstall --target local_lib git+https://github.com/jaraco/path.git >> path_install.log
echo \n >> path_install.log
if [ $? -eq 0 ]; then
    export PYTHONPATH=$(pwd)/local_lib
    python my_program.py
else
    echo "Installation failed, check the logs in local_lib/path_install.log"
fi