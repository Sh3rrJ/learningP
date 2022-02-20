import os
import requests
from bs4 import BeautifulSoup


def txt_name(s):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~—"
    for char in s:
        if char in punctuation:
            s = s.replace(char, '')
    s = s.replace('  ', ' ').strip()

    return "_".join(s.split(' ')) + '.txt'


page_number = int(input())
article_type = input()
saved_articles = []
base_path = os.getcwd()
url_base = 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page='

for n in range(1, page_number+1):
    os.mkdir('Page_' + str(n))
    os.chdir('Page_' + str(n))

    request = requests.get(url_base + str(n))
    soup = BeautifulSoup(request.content, 'html.parser')
    articles = soup.find_all('article')

    for article in articles:
        if article.find('span', class_="c-meta__type").text == article_type:
            article_url = 'https://www.nature.com' + article.find('a').get('href')
            request = requests.get(article_url)
            article_soup = BeautifulSoup(request.content, 'html.parser')

            txt_title = txt_name(article_soup.find('title').text)
            saved_articles.append(txt_title)
            file = open(txt_title, 'wb')
            article_body = article_soup.find('div', class_="c-article-body u-clearfix")
            file.write(article_body.text.encode('UTF-8'))
            file.close()

    os.chdir(base_path)

print('Saved articles:\n', saved_articles)

