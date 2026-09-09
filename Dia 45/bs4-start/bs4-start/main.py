from bs4.builder._htmlparser import BeautifulSoupHTMLParser
from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get("href")
    upvote = article_tag.get("score")

    article_texts.append(text)
    article_links.append(link)

print(article_texts)
print(article_links)
