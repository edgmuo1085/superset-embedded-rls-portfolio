# Utiliza una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt requirements.txt
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Variables de entorno
ENV SUPERSET_URL=http://localhost:8088 \
    SUPERSET_ADMIN_USER=admin \
    SUPERSET_ADMIN_PASSWORD=admin \
    SUPERSET_DASHBOARD_ID=d5f8b9de-a936-4c69-aa7a-04401fabb40c \
    SUPERSET_RLS_ROLE_NAME=Gamma \
    FRONTEND_URL=http://localhost:3002

# Expone el puerto en el que se ejecutará la API
EXPOSE 8100

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8100"]
