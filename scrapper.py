#!/usr/bin/env python3

import sys
import requests as req
from bs4 import BeautifulSoup

HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'accept-language': 'en',
    'accept-encoding': 'utf-8'
}

def get_twitter_followers(account):
    """ Get the number of the followers of a Twitter account """

    resp = req.get(f'https://twitter.com/{account}', HEADERS)
    soup = BeautifulSoup(resp.text, 'lxml')

    spans = soup.select('span.ProfileNav-value')

    return spans[2]['data-count']


if __name__ == '__main__':
    print({
        sys.argv[1]: get_twitter_followers(sys.argv[1])
    })