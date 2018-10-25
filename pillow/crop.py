#!/usr/bin/env python3
from PIL import Image 

try:
    img = Image.open("images/chinchilla.jpg")
    
    # pixel de inicio en X, pixel de inicio en Y, pixeles a cortar en X, pixeles a cortar en Y
    box = (300, 100, 500, 400)
    img = img.crop(box)

    img.show()
except IOError:
    print("No es posible abrir la imagen")