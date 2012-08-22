#!/bin/bash 

git pull -q
git reset -q --hard HEAD

make pdf &> /dev/null
echo "Content-type: application/pdf"
echo
cat bmh-cv.pdf
