#! /bin/bash

echo "You have selected $1. Executing script."
sleep 1

node "puppeteer-scripts/$1"

if [ $? -eq 0 ];
    then echo "Script executed success."
elif [ $? -eq 1 ];
    then echo "Script execution failed."
fi

