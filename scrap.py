import requests

from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        titles = links[idx].getText()
        href = links[idx].get('href', None)
        hn.append({'title': titles, 'link': href})
        print(hn)
    return hn


create_custom_hn(links, subtext)
