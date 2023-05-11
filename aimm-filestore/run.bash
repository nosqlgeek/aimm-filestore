#!/bin/zsh

# Important: Please change the following settings!
export PATH=$PATH:$HOME/Library/Python/3.9/bin
export FS_DATA_FOLDER=$HOME/tmp/data
export FS_ACCESS_KEY=test
export FS_ACCESS_SECRET=5ccdc06e9dfece4b67a531e2dc83e4b9

# Production deployment with TLS
gunicorn --certfile ./.ssh/cert.pem --keyfile ./.ssh/key.pem filestore:app