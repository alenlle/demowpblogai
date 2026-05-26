# AI Powered WordPress Auto Publisher

## Features

- Automatic keyword processing
- SERP scraping
- AI article generation using Groq
- WordPress publishing
- Featured image generation
- Yoast SEO support
- GitHub Actions automation
- SQLite tracking system

---

# Installation

```bash
git clone YOUR_REPO_URL
cd ai_wp_blog_publisher

pip install -r requirements.txt
```

---

# Environment Setup

Copy:

```bash
cp .env.example .env
```

Fill all API keys.

---

# WordPress Setup

1. Enable REST API
2. Install Yoast SEO
3. Create Application Password

WordPress:

Users → Profile → Application Passwords

---

# GitHub Secrets

Add:

- GROQ_API_KEY
- WORDPRESS_SITE_URL
- WORDPRESS_USERNAME
- WORDPRESS_APP_PASSWORD
- PEXELS_API_KEY
- PIXABAY_API_KEY

GitHub:

Repo → Settings → Secrets and Variables → Actions

---

# Add Keywords

Edit:

keywords/keywords.txt

Example:

```txt
best seo tools
technical seo checklist
```

---

# Run Locally

```bash
python main.py
```

---

# Run Scheduler

```bash
python scheduler/run_scheduler.py
```

---

# GitHub Actions Cron

Runs every 6 hours automatically.

You can also manually trigger workflow_dispatch.

---

# Future Improvements

- Semantic internal linking
- Multi-language support
- Google Search Console indexing
- AI image captions
- Auto category mapping