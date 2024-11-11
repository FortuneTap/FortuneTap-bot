# Usa la imagen oficial de Python
FROM python:3.10

# Instala las dependencias del sistema para Playwright
RUN apt-get update && apt-get install -y \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0

# Instala las dependencias de Python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Instala Playwright y sus navegadores
RUN pip install playwright && playwright install --with-deps

# Copia los archivos de la aplicación
COPY . .

# Expone el puerto de la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]