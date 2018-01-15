import os
import PIL
from PIL import Image

input_directory = "/home/nayeem/Desktop/photos"
output_directory = "/home/nayeem/Desktop/resized"

width = 1280
height = 960

for file in os.listdir(input_directory):
    if file.endswith(".jpg"):
        print("Resizing " + file)        
        img = Image.open(os.path.join(input_directory, file))
        img = img.resize((width, height), PIL.Image.ANTIALIAS)
        img.save(os.path.join(output_directory, file))
