import sys
import os
from premailer import transform

def render_template(template, **kwargs):
    with open(template, 'r') as file:
        return file.read()

if len(sys.argv) < 2:
        print('Please pass the template name as arguement')
else:
        template = sys.argv[1]
        html = transform(render_template(template))
        output_directory = "output/" + os.path.dirname(template)
        if not os.path.exists(output_directory):
                os.makedirs(output_directory)
        output_file = os.path.join(output_directory, os.path.basename(template))
        with open(output_file, "w") as new_file:
                new_file.write(html)
