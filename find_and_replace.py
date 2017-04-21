import os

location = '/home/shakil/Desktop/abc/'
file_type = 'php'
text_to_replace = '<? '
replace_with = '<?php '

files = os.listdir(location)
for file_name in files:  
    if file_name.endswith(file_type):
        file_name =  os.path.realpath(file_name)
        with open(file_name, 'r') as file :
            content = file.read()
        content = content.replace(text_to_replace, replace_with)
        with open(file_name, 'w') as file:
            file.write(filedata)

