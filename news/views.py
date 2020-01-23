from django.shortcuts import render, redirect
import urllib3
import requests
from bs4 import BeautifulSoup
from .models import Headline, UserProfile
from datetime import datetime, timezone

urllib3.disable_warnings()


def news_list(request):

    all_news = Headline.objects.all()
    context = {
        'all_news': all_news
    }
    return render(request, 'news/news_list.html', context)


def scrape(request):

    user_p = UserProfile()
    user_p.user = request.user
    user_p.last_scrape = datetime.now(timezone.utc)
    user_p.save()

    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 "
                                     "(KHTML, like Gecko) Mobile/7B405Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS "
                                     "X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405"}

    url = 'https://www.theonion.com/'
    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html.parser")

    section = soup.find('div', {'class': 'sc-1plvju9-0 fGFCYh'})

    titles = section.find_all_next('h4', {'class': 'kbLSgc'})
    links = [l.parent.get('href') for l in titles]

    for title, link in zip(titles, links):
        headline = Headline()
        headline.title = title.text
        headline.url = link
        headline.save()

    return redirect('/')

