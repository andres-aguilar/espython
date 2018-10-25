#!/usr/bin/env python3
from PIL import Image 

try:
    img = Image.open("images/chinchilla.jpg")
    
    # Rota la imagen X grados y redimensiona ajustando al ancho resultante
    img = img.rotate(40, expand=True)
    img = img.transpose( Image.ROTATE_90 )  # Rota la imagen en 90 grados

    img.show()
except IOError:
    print("No es posible abrir la imagen")