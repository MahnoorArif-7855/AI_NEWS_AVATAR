# 📰 AI News Avatar Pipeline


## 📌 Overview

The **AI News Avatar Pipeline** is an end-to-end automated system that transforms raw online news articles into a professional, AI-generated video news broadcast. The pipeline integrates web scraping, Large Language Model (LLM)–based summarization, script generation, and AI avatar video synthesis into a FastAPI-based application.

The project demonstrates practical AI engineering skills including prompt engineering, API integration, asynchronous processing, and modular backend design.

---

## 🧠 System Workflow

1. News Extraction – Scraping reputable online news sources  
2. LLM Summarization – Generating concise, factual summaries  
3. Script Generation – Producing a broadcast-style news script  
4. Avatar Video Synthesis – Rendering a lip-synced AI news anchor video  
5. API Interface – Managing execution and monitoring via FastAPI  

Each component is independently replaceable and scalable.

---

## 🏗️ Architecture & Components

### Data Ingestion (News Scraping)

- Uses `Requests` and `newspaper3k`
- Extracts article title, cleaned text, and source URL
- Outputs structured JSON data

### LLM-Based Summarization

- Uses OpenAI / Gemini APIs
- Produces neutral, factual summaries (3–4 sentences)
- Prevents hallucinations and speculation

### Script Generation

- Professional TV news anchor tone
- 30–45 seconds duration
- 75–110 words (140–160 WPM)

### Avatar Video Generation

- Integrates with third-party avatar APIs (e.g., D-ID)
- Asynchronous rendering with polling
- Outputs downloadable 1080p MP4 video

---

## 🔌 Backend API

| Endpoint | Method | Input | Output | Pipeline Stage |
|--------|--------|------|--------|---------------|
| /news/scrape | GET | None | Articles (Title, Text, URL) | Data Ingestion |
| /news/summarize | POST | Articles | Neutral Summaries | LLM Processing |
| /news/script | POST | Summaries | News Script | Script Generation |
| /news/video | POST | Script | Video URL & Status | Media Synthesis |
| /news/run | POST | Keyword / URL | Full Pipeline Output | End-to-End |

---

## ⚙️ Setup & Installation

### Requirements
- Python 3.10+
- FastAPI
- newspaper3k
- OpenAI / Gemini API
- Avatar Video API (D-ID)

### Installation
```bash
pip install -r requirements.txt
```

### Environment Variables
```env
OPENAI_API_KEY=your_key_here
DID_API_KEY=your_key_here
```

### Run Server
```bash
uvicorn main:app --reload
```

---

## 📁 Project Structure

```bash
ai_news_avatar/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   └── services/
│       ├── scraper.py
│       ├── llm.py
│       ├── script_writer.py
│       ├── avatar.py
│       └── storage.py
├── data/
├── outputs/
├── requirements.txt
└── README.md`
```
---

## ✅ Outcome

This project demonstrates a complete AI-driven media pipeline that converts unstructured news content into a polished, avatar-based video broadcast. It is production-ready and extensible for future enhancements such as multilingual support and real-time updates.
