import requests
from config.settings import WORDPRESS_SITE_URL

def fetch_existing_posts():
    url = f"{WORDPRESS_SITE_URL}/wp-json/wp/v2/posts?per_page=20"
    res = requests.get(url, timeout=30)

    if res.status_code != 200:
        return []

    return res.json()

def add_internal_links(content):
    posts = fetch_existing_posts()

    for post in posts[:3]:
        title = post["title"]["rendered"]
        link = post["link"]

        if title.lower() in content.lower():
            content += f'\n<p>Related: <a href="{link}">{title}</a></p>'

    return content