import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mergedlinks = links + links2
mergedsubtext = subtext + subtext2


def sorted_stories(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


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

    return sorted_stories(hn)


pprint.pprint(create_custom_hn(mergedlinks, mergedsubtext))
