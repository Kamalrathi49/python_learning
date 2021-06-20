import requests

from bs4 import BeautifulSoup

res = requests.get("https://www.youtube.com/")

soup = BeautifulSoup(res.text, "html.parser")
