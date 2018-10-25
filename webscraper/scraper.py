#! /usr/bin/python3

from __future__ import print_function
from bs4 import BeautifulSoup as bs
from requests import get
from threading import Thread

GOOGLE_NEWS = "https://news.google.com.mx/"


def set_robot(article):
    title = article.find('span')
    print(title.get_text())


def get_site(site):
    """ get_site

    returns: A beautifulSoup4 object
    """
    res = get(site)

    if res.status_code == 200:
        return bs(res.text, 'html.parser')


def scraping_site():
    soup = get_site(GOOGLE_NEWS)

    if soup is not None:
        articles = soup.find_all('a', {'class': 'ipQwMb Q7tWef'})

        for article in articles:
            robot = Thread(name='set_robot', target=set_robot, args=(article,))
            robot.start()


def main():
    scraping_site()

if __name__ == '__main__':
    main()