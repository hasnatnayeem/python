import requests
import sys

url = sys.argv[1];
file_name = sys.argv[2]

res = requests.get(url)
with open(file_name, "wb") as f: # wb for writing binary data
    f.write(res.content) # content is used for retrieving bytes instead of regular strings


# Command to run this program
# python image-download.py http://image-url.com/.... name_of_the_file