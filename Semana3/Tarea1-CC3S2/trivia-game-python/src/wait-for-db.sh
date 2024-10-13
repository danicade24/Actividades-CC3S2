#!/bin/sh
until nc -z db 5432; do
  echo "Esperando a la base de datos..."
  sleep 1
done
echo "Base de datos está lista, ejecutando el script."
sleep 5  # Agrega un pequeño retraso adicional
exec "$@"
