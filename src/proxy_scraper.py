import requests
from bs4 import BeautifulSoup

def scrape_proxies():
    proxies = []
    # Daftar sumber proxy online
    sources = [
        "https://www.sslproxies.org/",
        "https://free-proxy-list.net/",
        "https://www.us-proxy.org/",
    ]
    
    for source in sources:
        response = requests.get(source)
        soup = BeautifulSoup(response.text, 'html.parser')
        for row in soup.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) > 6:
                ip = cols[0].text
                port = cols[1].text
                protocol = "https" if "yes" in cols[6].text.lower() else "http"
                proxies.append(f"{protocol}://{ip}:{port}")
    return proxies
