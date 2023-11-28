#!/bin/sh
# wait-for-api.sh

set -e

api_host="audiotopic-api"
api_port=8000

until nc -z $api_host $api_port; do
  echo "Aguardando o audiotopic-api ficar disponível..."
  sleep 1
done

echo "audiotopic-api está disponível. Iniciando o audiotopic-app."
exec "$@"
