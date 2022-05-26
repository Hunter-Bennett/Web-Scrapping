import requests
from bs4 import BeautifulSoup
import pprint

# .titlelink == .storylink
res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

link = soup.select('.titlelink')
subtext = soup.select('.subtext')
link2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')

mega_link = link + link2
mega_subtexts = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['vote'], reverse=True)

def create_custom_hn(link, subtext):
    hn = []
    for idx, item in enumerate(link):
        title = link[idx].getText()
        href = link[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title' : title, 'link': href, 'vote': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_link, mega_subtexts))