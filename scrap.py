import requests
from bs4 import BeautifulSoup
import pprint

url = "https://news.ycombinator.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        titles = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({'title': titles, 'link': href, "votes": points})
    return hn


pprint.pprint(create_custom_hn(links, subtext))
