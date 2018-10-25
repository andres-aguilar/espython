#!/usr/bin/env python3
from PIL import Image

try:
    img = Image.open("images/chinchilla.jpg")
    copy = img.resize( (200, 200) )  # Duplicamos la imagen y le cambiamos el tamaño
    
    img.paste(copy, (100, 100) ) # Pagamos la imagen pequeña dentro de la original, coordenadas

    img.show()
except IOError:
    print("No es posible abrir la imagen")