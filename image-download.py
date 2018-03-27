import requests

url = "http://localhost/test_image.jpg";
res = requests.get(url)
with open("downloaded_image.jpg", "wb") as f: # wb for writing binary data
    f.write(res.content) # content is used for retrieving bytes instead of regular strings