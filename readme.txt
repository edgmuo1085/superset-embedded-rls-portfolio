### Comandos para el backend-app Docker
docker build -t project/backend-set:0.0.1 .
docker stop back-set || true
docker rm back-set || true
docker run -d -p 8100:8100 --restart always --name back-set project/backend-set:0.0.1


### Comandos para el frontend-app Docker
docker build -t project/front-superset:0.0.1 --build-arg TYPE=dev .
docker stop ng-superset || true
docker rm ng-superset || true
docker run -d -p 3002:80 --name ng-superset project/front-superset:0.0.1


### Ejecutar las variables de entorno para el sistema
export METADATA_DB_URI="postgresql+psycopg2://superset:superset@db:5432/superset" 
export SUPERSET_SECRET_KEY="1" 
export SUPERSET_JWT_SECRET="1" 
