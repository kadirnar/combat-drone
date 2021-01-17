from PIL import Image
import os
import PIL
import glob


images = [file for file in os.listdir() if file.endswith(('jpeg', 'png', 'jpg'))]
for image in images:
    img = Image.open(image)
    img.thumbnail((640,640))
    img.save("resized_"+image, optimize=True, quality=40)