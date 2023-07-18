from bs4 import BeautifulSoup
import requests

class WebScraping:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        req = requests.get(self.url)
        soup = BeutifulSoup(req.content, 'html.parser')
        return soup
