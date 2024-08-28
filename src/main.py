import time
from proxy_scraper import scrape_proxies
from proxy_checker import check_proxies
from utils import save_proxies
from config import UPDATE_INTERVAL

def main():
    while True:
        proxies = scrape_proxies()
        valid_proxies = check_proxies(proxies)
        save_proxies(valid_proxies)
        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()
