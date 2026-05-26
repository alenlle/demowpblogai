import sqlite3
from pathlib import Path

DB = "database/blog.db"
KEYWORD_FILE = "keywords/keywords.txt"

def sync_keywords():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    if Path(KEYWORD_FILE).exists():
        with open(KEYWORD_FILE, "r", encoding="utf-8") as f:
            keywords = [k.strip() for k in f.readlines() if k.strip()]

        for keyword in keywords:
            cur.execute(
                "INSERT OR IGNORE INTO keywords(keyword) VALUES(?)",
                (keyword,)
            )

    conn.commit()
    conn.close()

def get_next_keyword():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "SELECT id, keyword FROM keywords WHERE processed = 0 LIMIT 1"
    )
    row = cur.fetchone()
    conn.close()

    return row

def mark_processed(keyword_id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "UPDATE keywords SET processed = 1 WHERE id = ?",
        (keyword_id,)
    )

    conn.commit()
    conn.close()