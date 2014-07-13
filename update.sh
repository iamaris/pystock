#!/bin/bash     
echo "a" >> a.sh 
#env -i git add *
#env -i git commit -am "update"
git add *
git commit -am "update"
git push origin master
git config --global credential.helper 'cache --timeout=3600'

