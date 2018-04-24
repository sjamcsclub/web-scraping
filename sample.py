import requests
from bs4 import BeautifulSoup as soup

def get_url(url):
    return soup(
        requests.get(url).text
    )
