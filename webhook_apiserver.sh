#!/bin/bash
cd /opt/apiserver
echo "pulling from apiserver:dev"
git pull origin dev
echo "pull successfully from dev"
echo "restart server..."
service uwsgi restart
