FROM python:3.11-slim

WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las librerías necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el contenido del proyecto
COPY . .

# Exponer los puertos que usan FastAPI y Streamlit
EXPOSE 8000
EXPOSE 8501