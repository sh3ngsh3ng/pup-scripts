#! /bin/bash

echo "You have selected $1. Executing script."
sleep 1

<<<<<<< HEAD
node "puppeteer-scripts/$1"

if [ $? -eq 0 ];
    then echo "Script executed success."
elif [ $? -eq 1 ];
    then echo "Script execution failed."
=======
echo "Puppeteer is currently live..."
node "puppeteer-scripts/$1"

if [ $? -eq 0 ];
    then echo "Script: $1 executed successfully. Browser closed."
elif [ $? -eq 1 ];
    then echo "Script: $1 execution failed."
>>>>>>> 1233620253b76c50efb489c9c8b5f65a7a26404f
fi

