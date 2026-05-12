import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def summarize_news(news_articles):

    headlines = "\n".join(
        [article["title"] for article in news_articles]
    )

    prompt = f"""
    You are a financial analyst.

    Summarize the following stock news:

    {headlines}

    Give:
    1. Summary
    2. Market sentiment
    3. Key risks
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content