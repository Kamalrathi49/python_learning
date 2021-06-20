import requests

from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

print(soup.find(id="score_27569772"))
