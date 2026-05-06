import os
from dotenv import load_dotenv
from openai import OpenAI

# load env variables
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if API_KEY is None:
    raise ValueError("OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=API_KEY)


def call_llm(prompt, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content
