# Imagen base
FROM python:3.9-slim-buster

# Instalar dependencias de tesseract
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
 && rm -rf /var/lib/apt/lists/*

# Copiar el código de la aplicación
WORKDIR /app
COPY . /app

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Establecer la variable de entorno para el ejecutable de tesseract
ENV TESSERACT_CMD=/usr/share/tesseract-ocr

# Comando predeterminado para ejecutar la aplicación
CMD [ "python", "app.py" ]
