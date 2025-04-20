import requests
from bs4 import BeautifulSoup

def search(query):
    url = f"https://filmywap.support/?s={query.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for link in soup.select(".result-item h3 a"):
        title = link.text.strip()
        href = link['href']
        results.append(f"🎬 **{title}**\n{href}")
    return results[:3]
