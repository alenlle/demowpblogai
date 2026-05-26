def add_external_links(content):
    links = [
        ("Wikipedia SEO", "https://en.wikipedia.org/wiki/Search_engine_optimization"),
        ("Google Search Central", "https://developers.google.com/search")
    ]

    for text, link in links:
        content += f'\n<p><a href="{link}" target="_blank">{text}</a></p>'

    return content