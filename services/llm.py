import openai
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai.api_key)

if not openai.api_key:
    raise RuntimeError("OPENAI_API_KEY not set in .env")


def summarize(text: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "You summarize news articles factually and neutrally."
            },
            {
                "role": "user",
                "content": f"Summarize the following article in 3–4 sentences:\n{text}"
            }
        ],
    )

    return response.output_text