import requests
from bs4 import BeautifulSoup as soup

def get_url(url):
    return soup(
        requests.get(url).text
    )

t = get_url("https://jamhacks.ca")

landing = t.find(
  "div",
  {
    "id" : "landing-content"
  }
)

date = landing.find(
  "h2"
)

print(
  date.get_text()
)
