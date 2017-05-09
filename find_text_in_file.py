import os
import mimetypes


def is_binay_file(filepathname):
    textchars = bytearray([7,8,9,10,12,13,27]) + bytearray(range(0x20, 0x7f)) + bytearray(range(0x80, 0x100))
    is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))

    if is_binary_string(open(filepathname, 'rb').read(1024)):
       return True
    else:
       return False


counter = 0
for root, dirs, files in os.walk("/home/shakil/Desktop/italc-3.0.3"):
    for f in files:
        file_name = root + '/' + f
        with open(file_name, 'r') as file :
            if not is_binay_file(file_name):         
                try:
                    content = file.read()
                    if content.find("2004-2016") != -1:
                        counter += 1
                        print (file_name + '\n\n')
                except UnicodeDecodeError:
                    continue   
if counter > 1:   
    print (str(counter) + " files found") 
elif counter == 1:
    print (str(counter) + " file found")            
else:
    print ("No file found")











