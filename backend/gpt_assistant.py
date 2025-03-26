import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

DEFAULT_MODEL = "gpt-4"
FALLBACK_MODEL = "gpt-3.5-turbo"

def ask_gpt(prompt: str, confidence_threshold: float = 0.7) -> str:
    try:
        response = openai.ChatCompletion.create(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content
        confidence = response.usage.total_tokens / 8000

        if confidence < confidence_threshold:
            fallback_response = openai.ChatCompletion.create(
                model=FALLBACK_MODEL,
                messages=[{"role": "user", "content": prompt}]
            )
            return f"[GPT-4 fallback til 3.5]\n{fallback_response.choices[0].message.content}"

        return reply
    except Exception as e:
        return f"GPT-feil: {str(e)}"
