from markdown import markdown

from database.init_db import init_db
from generators.keyword_manager import (
    sync_keywords,
    get_next_keyword,
    mark_processed
)

from seo.serp_scraper import scrape_serp
from generators.content_generator import (
    generate_title,
    generate_article,
    generate_meta
)

from generators.image_generator import generate_feature_image
from seo.internal_linker import add_internal_links
from seo.external_links import add_external_links
from wordpress.wordpress_publisher import publish_post
from utils.logger import log

def run_workflow():
    init_db()
    sync_keywords()

    data = get_next_keyword()

    if not data:
        log("No keywords remaining.")
        return

    keyword_id, keyword = data

    log(f"Processing keyword: {keyword}")

    serp = scrape_serp(keyword)

    title = generate_title(keyword)

    article = generate_article(keyword, serp)

    article = add_internal_links(article)
    article = add_external_links(article)

    html_content = markdown(article)

    meta = generate_meta(keyword)

    meta_title = title[:60]
    meta_desc = meta[:150]

    image_path = generate_feature_image(title)

    result = publish_post(
        title=title,
        content=html_content,
        meta_title=meta_title,
        meta_desc=meta_desc,
        featured_image=image_path
    )

    mark_processed(keyword_id)

    log(f"Published successfully: {result['link']}")