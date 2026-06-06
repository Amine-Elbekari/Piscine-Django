#!/bin/sh

link=$1
if [ -z $link ]; then
        echo "Error: [USAGE]: ./myawesomescript.sh YOUR_SHORT_LINK"
        exit 1
elif [ $# -gt 1 ]; then
        echo "Error: This Script accepts only one argument."
        exit 1
else
    curl -s $link | cut -d ';' -f 1 | grep -E -o 'https?://[^/]*/'
fi