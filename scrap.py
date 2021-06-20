import requests

from bs4 import BeautifulSoup

url = "https://www.youtube.com/"

res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

print(soup)
