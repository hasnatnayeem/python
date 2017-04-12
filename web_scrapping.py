import requests
from bs4 import BeautifulSoup

daily_star = requests.get('http://thedailystar.net')
parsed_html = BeautifulSoup(daily_star.text, 'lxml')
headlines = parsed_html.find_all('h5')

word_count = {}

for headline in headlines:
    headline_words = headline.text.split()
    for word in headline_words:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1

for word in word_count:
    print("*{0}* -> {1}".format(word, word_count.get(word)))

