import openai
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_script(summaries_text: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "You are a professional TV news anchor."
            },
            {
                "role": "user",
                "content": f"""
                Write a professional news anchor script from the following summaries.

                Requirements:
                - 30–45 seconds spoken length
                - Professional, conversational tone
                - Start with a greeting and top headlines
                - Mention each story once
                - End with a short closing line

                Summaries:
                {summaries_text}
"""
            }
        ],
    )

    return response.output_text
