#!/usr/bin/env python3
from PIL import Image, ImageFilter

try:
    img = Image.open("images/chinchilla.jpg")
    
    img = img.filter( ImageFilter.BLUR )  # Aplicar un filtro BLUR a la imagen

    img.show()
except IOError:
    print("No es posible abrir la imagen")