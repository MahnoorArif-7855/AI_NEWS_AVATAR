from newspaper import Article

def scrape_articles(urls):
    articles = []

    for url in urls:
        try:
            article = Article(url)
            article.download()
            article.parse()

            if not article.text.strip():
                continue

            articles.append({
                "title": article.title,
                "text": article.text,
                "url": url
            })

        except Exception as e:
            print(f"[SCRAPE ERROR] {url}: {e}")

    return articles
