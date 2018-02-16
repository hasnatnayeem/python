import os
from PIL import Image


location = '/media/shakil/.....'

files = os.listdir(location)
for file_name in files:
    if file_name.endswith(".jpg"):
        img = Image.open(file_name)
        img = img.resize((100,200), Image.ANTIALIAS)
        img.save(file_name.replace(".jpg", ".pdf"), "PDF", quality=100)
