import requests

def duck_search(query):
    url = f"https://duckduckgo.com/?q={query}"
    
    headers = {"User-Agent": "Mozilla/5.0"}
    
    proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050",
    }
    
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

# Example usage
if __name__ == "__main__":
    duck_search("Maxwell Fung")