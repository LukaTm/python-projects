from bs4 import BeautifulSoup
import requests

class Artists:
    def __init__(self,soup):
        self.soup = soup

    def artists(self):
        artist_names = self.soup.find_all(name='span',class_='c-label')
        only_words = [x.getText().strip() for x in artist_names]
        new = [x for x in only_words if not x.isnumeric() and x != '-'] # !!!!!!!!!!!!!!!!!!!!!!!!!! IS NUMERIC
        return new


