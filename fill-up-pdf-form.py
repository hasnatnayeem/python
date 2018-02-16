from fdfgen import forge_fdf
import os

pdf_file = "form.pdf"
tmp_file = "data.pdf"
output_file  = "output.pdf"

fields = [('Identification no','123456'),('Yr Model','54321')]

fdf = forge_fdf("", fields, [], [], [])
fdf_file = open(tmp_file,"wb")

fdf_file.write(fdf)
fdf_file.close()

cmd = 'pdftk "{0}" fill_form "{1}" output "{2}"  flatten'.format(pdf_file, tmp_file, output_file);
os.system(cmd)

os.remove(fdf_file.name)
