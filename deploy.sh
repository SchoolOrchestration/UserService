#!/bin/bash
env='staging'
read -p "Deploy to: ${1:-$env} [Y/n]: " -n 1 -r
echo    # (optional) move to a new line

if [[ $REPLY =~ ^[Yy]$ ]]
then
  # echo "docker-compose -f docker-compose.school.yml -e ENV=${1:-$env} up"
  export ENV=${1:-$env}
  docker-compose -f docker-compose.school.yml up
else
  echo "Doing nothing."
  echo "Usage: sh ./deploy.sh {staging|production}"
fi
