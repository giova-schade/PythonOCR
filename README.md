OCR con Python y Tesseract en Docker
Este proyecto es una aplicación de reconocimiento óptico de caracteres (OCR) que utiliza Python y Tesseract para reconocer texto en imágenes. La aplicación está diseñada para ser ejecutada en un contenedor de Docker, lo que facilita la instalación y el uso en diferentes sistemas operativos.

Requisitos
Antes de comenzar, asegúrese de tener Docker instalado en su sistema. Si aún no tiene Docker instalado, puede seguir las instrucciones de la documentación oficial para instalar Docker en su sistema: https://docs.docker.com/get-docker/.

Instalación
Para instalar la aplicación OCR, siga estos pasos:

Clone este repositorio en su máquina local:

bash

git clone https://github.com/giova-schade/PythonOCR.git

Vaya al directorio del repositorio clonado:

bash

cd PythonOCR
Construya la imagen de Docker utilizando el siguiente comando:


docker build -t mi-imagen-ocr .
Este comando construirá una imagen de Docker llamada mi-imagen-ocr utilizando el archivo Dockerfile incluido en el repositorio. Tenga en cuenta que puede cambiar el nombre de la imagen según sus necesidades.

Tenga en cuenta que la construcción de la imagen puede llevar algún tiempo, ya que Docker descarga e instala todas las dependencias necesarias para la aplicación.

Ejecute la aplicación en un contenedor de Docker utilizando el siguiente comando:



docker run -p 5000:5000 mi-imagen-ocr
Este comando ejecutará un contenedor de Docker utilizando la imagen mi-imagen-ocr que acabamos de construir. El parámetro -p indica que se deben redirigir los puertos del contenedor al sistema host, lo que permite acceder a la aplicación a través de su navegador web. El número 5000 es el puerto en el que se ejecuta la aplicación en el contenedor, y puede cambiarlo si lo desea.

Abra su navegador web y vaya a http://localhost:5000 para acceder a la aplicación OCR. Si está ejecutando Docker en una máquina virtual, asegúrese de utilizar la dirección IP de la máquina virtual en lugar de localhost.

Uso
Una vez que haya instalado la aplicación OCR y la haya ejecutado en un contenedor de Docker, puede utilizarla para reconocer texto en imágenes. Para utilizar la aplicación, siga estos pasos:

Abra su navegador web y vaya a http://localhost:5000 para acceder a la aplicación OCR.

Haga clic en el botón "Seleccionar archivo" y seleccione la imagen que desea procesar.

Haga clic en el botón "Procesar imagen" para iniciar el proceso de OCR.

Espere a que la aplicación procese la imagen y muestre el resultado del OCR en la página.

Si desea procesar otra imagen, puede hacer clic en el botón "Seleccionar archivo" nuevamente y repetir el proceso.

Contribuciones# PythonOCR
