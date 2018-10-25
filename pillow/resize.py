#!/usr/bin/env python3
from PIL import Image 

try:
    img = Image.open("images/chinchilla.jpg")
    
    print(img.size)
    img = img.resize((img.width//2, img.height//2))
    img.show()
except IOError:
    print("No es posible abrir la imagen")