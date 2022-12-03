import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """ fetch the html from url """
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    req = requests.get(url, headers=headers)

    if req.status_code != 200:
        raise Exception('Failed to fetch url')

    return req.text

def get_html_parser(html):
    """ return html parser """
    soup = BeautifulSoup(html, 'html.parser')
    return soup