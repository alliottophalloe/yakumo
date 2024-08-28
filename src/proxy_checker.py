import requests

def check_proxies(proxies):
    valid_proxies = []
    for proxy in proxies:
        try:
            response = requests.get("https://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=5)
            if response.status_code == 200:
                valid_proxies.append(proxy)
        except:
            continue
    return valid_proxies
