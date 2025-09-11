#!/bin/bash
# Script para regenerar claves seguras para Superset

set -e

# Archivo .env en el directorio actual
ENV_FILE=".env"

# Función para generar claves seguras con Python
generate_secret() {
  python3 -c "import secrets; print(secrets.token_urlsafe(64))"
}

# Generar nuevas claves
NEW_SUPERSET_SECRET_KEY=$(generate_secret)
NEW_SUPERSET_JWT_SECRET=$(generate_secret)

# Crear archivo .env si no existe
if [ ! -f "$ENV_FILE" ]; then
  echo "Creando $ENV_FILE..."
  touch "$ENV_FILE"
fi

# Eliminar claves viejas del archivo
sed -i '/^SUPERSET_SECRET_KEY=/d' "$ENV_FILE"
sed -i '/^SUPERSET_JWT_SECRET=/d' "$ENV_FILE"

# Escribir nuevas claves
{
  echo "SUPERSET_SECRET_KEY=$NEW_SUPERSET_SECRET_KEY"
  echo "SUPERSET_JWT_SECRET=$NEW_SUPERSET_JWT_SECRET"
} >> "$ENV_FILE"

echo "✅ Nuevas claves generadas y guardadas en $ENV_FILE"

echo "SUPERSET_SECRET_KEY=${NEW_SUPERSET_SECRET_KEY}"
echo "SUPERSET_JWT_SECRET=${NEW_SUPERSET_JWT_SECRET}"

echo "⚠️ Recuerda reiniciar tus contenedores:"
echo "   make down && make build"