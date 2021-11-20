#!/bin/zsh

~/loadrc/dockerrc/killDockers.sh
rm -fr ./db_dir/
docker-compose up --build -d
watch ~/loadrc/sqlrc/xsql.sh select.sql
