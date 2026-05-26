import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def scrape_serp(keyword):
    headers = {"User-Agent": UserAgent().random}
    url = f"https://www.google.com/search?q={keyword.replace(' ', '+')}"
    res = requests.get(url, headers=headers, timeout=20)

    soup = BeautifulSoup(res.text, "lxml")

    results = []

    for h3 in soup.select("h3")[:5]:
        results.append(h3.get_text(strip=True))

    return results