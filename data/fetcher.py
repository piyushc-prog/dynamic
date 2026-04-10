import requests
from bs4 import BeautifulSoup

class DataFetcher:
    
    def fetch_from_url(self, url):
        headers = {"User-Agent": "Mozilla/5.0"}  
        response = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])
        
        return text