#!/bin/bash
branch=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
echo "Building Branch: $branch"
read -p "Create/update image ${1:-$branch} [Y/n]: " -n 1 -r
echo    # (optional) move to a new line

if [[ $REPLY =~ ^[Yy]$ ]]
then
  docker build -t schoolorchestration/userservice:${1:-$branch} .
  docker push schoolorchestration/userservice:${1:-$branch}
fi
