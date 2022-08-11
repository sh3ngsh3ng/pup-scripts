#! /bin/bash

echo "You have selected $1. Executing script."
sleep 1

echo "Puppeteer is currently live..."
node "puppeteer-scripts/$1"

if [ $? -eq 0 ];
    then echo "Script: $1 executed successfully. Browser closed."
elif [ $? -eq 1 ];
    then echo "Script: $1 execution failed."
fi

