from pathlib import Path
from generators.groq_client import ask_groq

def load_prompt(name):
    return Path(f"prompts/{name}").read_text(encoding="utf-8")

def generate_title(keyword):
    prompt = load_prompt("title_prompt.txt").format(keyword=keyword)
    return ask_groq(prompt)

def generate_article(keyword, serp_data):
    prompt = load_prompt("article_prompt.txt").format(keyword=keyword)
    prompt += "\nSERP Context:\n" + "\n".join(serp_data)

    return ask_groq(prompt)

def generate_meta(keyword):
    prompt = f'''
Generate:
1. SEO Meta Title
2. SEO Meta Description

Keyword: {keyword}
'''

    return ask_groq(prompt)