import requests
from requests.auth import HTTPBasicAuth
from config.settings import (
    WORDPRESS_SITE_URL,
    WORDPRESS_USERNAME,
    WORDPRESS_APP_PASSWORD
)

auth = HTTPBasicAuth(
    WORDPRESS_USERNAME,
    WORDPRESS_APP_PASSWORD
)

def upload_image(image_path):
    media_url = f"{WORDPRESS_SITE_URL}/wp-json/wp/v2/media"

    with open(image_path, "rb") as img:
        headers = {
            "Content-Disposition": f"attachment; filename={image_path.name}",
            "Content-Type": "image/webp"  # FIX: required for WP REST API
        }

        response = requests.post(
            media_url,
            headers=headers,
            data=img,          # FIX: use data= not files= when Content-Type is set manually
            auth=auth,
            timeout=60
        )

    response.raise_for_status()
    return response.json()["id"]

def publish_post(title, content, meta_title, meta_desc, featured_image):
    media_id = upload_image(featured_image)

    post_url = f"{WORDPRESS_SITE_URL}/wp-json/wp/v2/posts"

    payload = {
        "title": title,
        "content": content,
        "status": "publish",
        "featured_media": media_id,
        "meta": {
            "_yoast_wpseo_title": meta_title,
            "_yoast_wpseo_metadesc": meta_desc
        }
    }

    response = requests.post(
        post_url,
        json=payload,
        auth=auth,
        timeout=60
    )

    response.raise_for_status()
    return response.json()
