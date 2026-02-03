from fastapi import FastAPI
import json
from dotenv import load_dotenv
import os
from services.llm import summarize
from services.scraper import scrape_articles
from services.script_writer import generate_script
from services.avatar import generate_avatar_video

from fastapi.templating import Jinja2Templates
from fastapi.requests import Request


load_dotenv()

app = FastAPI(title="AI News Avatar API")

NEWS_URLS = [
    "https://www.theguardian.com/world/live/2026/feb/03/russia-ukraine-europe-live-eu-us-military-plan-response-latest-news",
    "https://www.aljazeera.com/",
    "https://www.independent.co.uk/news/world/europe/",
    "https://www.freshnews.org/"
    "https://www.skysports.com/news-wire",
]

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )



@app.get("/news/scrape")
def scrape():
    articles = scrape_articles(NEWS_URLS)

    with open("data/articles.json", "w", encoding="utf-8") as f:
        import json
        json.dump(articles, f, ensure_ascii=False, indent=2)

    return articles


@app.post("/news/summarize")
def summarize_news():
    import json

    with open("data/articles.json", "r", encoding="utf-8") as f:
        articles = json.load(f)

    summaries = []
    for art in articles:
        summary = summarize(art["text"])
        summaries.append({
            "title": art["title"],
            "summary": summary,
            "url": art["url"]
        })

    with open("data/summaries.json", "w", encoding="utf-8") as f:
        json.dump(summaries, f, ensure_ascii=False, indent=2)

    return summaries


@app.post("/news/script")
def script():
    import json

    with open("data/summaries.json", "r", encoding="utf-8") as f:
        summaries = json.load(f)

    summaries_text = "\n".join(
        f"- {s['title']}: {s['summary']}" for s in summaries
    )

    script_text = generate_script(summaries_text)

    with open("data/script.txt", "w", encoding="utf-8") as f:
        f.write(script_text)

    return {"script": script_text}


@app.post("/news/video")
def video():
    with open("data/script.txt", "r", encoding="utf-8") as f:
        script_text = f.read()

    video_data = generate_avatar_video(script_text)

    return video_data


@app.post("/news/run")
def run_all():
    articles = scrape()
    summaries = summarize_news()
    script_data = script()
    video_data = video()

    return {
        "articles": articles,
        "summaries": summaries,
        "script": script_data["script"],
        "video": video_data
    }



