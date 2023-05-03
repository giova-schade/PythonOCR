import cv2
import pytesseract
import numpy as np
from PIL import Image
from flask import Flask, jsonify, request
import platform

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    os_name = platform.system()
    if os_name == "Windows":
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\Tesseract-OCR\\tesseract.exe'
    
    # Verificar si el archivo de imagen está presente en la solicitud
    if 'image' not in request.files:
        return jsonify({'error': 'Debe ingresar una imagen.'}), 400

    # Obtener la imagen enviada en el cuerpo de la solicitud
    img = cv2.imdecode(np.fromstring(request.files['image'].read(), np.uint8), cv2.IMREAD_COLOR)

    # Convertir a escala de grises y aplicar filtro gaussiano para reducir el ruido
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Aplicar umbral adaptativo para binarizar la imagen
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Aplicar erosión y dilatación para eliminar el ruido y mejorar la calidad de los caracteres
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    thresh = cv2.erode(thresh, kernel, iterations=0)
    thresh = cv2.dilate(thresh, kernel, iterations=0)
    # Convertir la imagen de OpenCV a formato de imagen de PIL
    img_pil = Image.fromarray(thresh)

    # Realizar OCR en la imagen usando Tesseract
    texto = pytesseract.image_to_string(img_pil)

    # Devolver el texto reconocido en formato JSON
    return jsonify({'texto': texto})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)
