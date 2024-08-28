import json

def save_proxies(proxies, file_path='data/proxies.json'):
    with open(file_path, 'w') as file:
        json.dump(proxies, file)

def load_proxies(file_path='data/proxies.json'):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
