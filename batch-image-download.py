import requests

for i in range(4):
    num = "0"
    num = "0" + str(i) if i < 10 else str(i)

    url = "http://sztafetapokolen.pl/img/sek/sekwencja" + num + ".jpg"
    file_name = "sekwencja" + num + ".jpg"
    print("Downloading " + url)
    response = requests.get(url)
    with open(file_name, "wb") as f:
        f.write(response.content)
