#!/bin/zsh
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

~/loadrc/dockerrc/killDockers.sh
rm -fr ./db_dir/
docker-compose up --build -d
watch ~/loadrc/sqlrc/xsql.sh select.sql
