from pathlib import Path
from generators.groq_client import ask_groq

def load_prompt(name):
    return Path(f"prompts/{name}").read_text(encoding="utf-8")

def generate_title(keyword):
    prompt = load_prompt("title_prompt.txt").format(keyword=keyword)
    return ask_groq(prompt).strip()

def generate_article(keyword, serp_data):
    prompt = load_prompt("article_prompt.txt").format(keyword=keyword)
    if serp_data:
        prompt += "\nSERP Context:\n" + "\n".join(serp_data)
    return ask_groq(prompt)

def generate_meta_title(keyword):
    prompt = f"Generate a concise SEO meta title (max 60 characters) for this keyword: {keyword}. Return only the title, no labels or explanation."
    return ask_groq(prompt).strip()

def generate_meta_desc(keyword):
    prompt = f"Generate a compelling SEO meta description (max 150 characters) for this keyword: {keyword}. Return only the description, no labels or explanation."
    return ask_groq(prompt).strip()
