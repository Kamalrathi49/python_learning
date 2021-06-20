import requests

from bs4 import BeautifulSoup

res = requests.get("https://www.youtube.com/")

BeautifulSoup(res.text, "html.parser")
