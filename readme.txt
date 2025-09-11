### Comandos para el backend-app Docker
docker build -t project/backend-set:0.0.20 .
docker stop back-set || true
docker rm back-set || true
docker run -d -p 8000:8000 --restart always --name back-set project/backend-set:0.0.20

### Ejecutar las variables de entorno para el sistema

export METADATA_DB_URI="postgresql+psycopg2://superset:superset@db:5432/superset" 
export SUPERSET_SECRET_KEY="1" 
export SUPERSET_JWT_SECRET="1" 
