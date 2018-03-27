import requests
import sys

url = "http://localhost/test.php"
data_dt = {"name" : "Nayeem", "age" : "24"}

res = requests.post(url, data = data_dt)

if (res.ok is False):
    sys.exit("A problem occurred")
    
print(res.text)