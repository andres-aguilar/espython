#!/usr/bin/env python3
from PIL import Image 

try:
    img = Image.open("images/chinchilla.jpg")
    print(img.mode)  # Imprime el modo en el que está la imagen
    # print(img.getpixel( (100, 200) ))  # Obtiene un pixel por medio de coordenadas

    img = img.convert("L")  # Conviente el modo de la imagen. en este caso a B/N
    img.save("images/chinchilla_bn.jpg")
except IOError:
    print("No es posible abrir la imagen")