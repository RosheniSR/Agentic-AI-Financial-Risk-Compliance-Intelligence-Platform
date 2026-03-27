import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def generate_explanation(prompt: str) -> str:
    try:
        print("🔥 Calling GROQ API...")

        # ✅ LIMIT INPUT SIZE (VERY IMPORTANT FIX)
        prompt = prompt[:3000]

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment")

        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a STRICT EU compliance assistant. "
                        "Always respond in MAXIMUM 2–3 lines only. "
                        "No bullet points, no numbering, no extra explanation."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            # 🔥 CONTROL OUTPUT SIZE
            max_tokens=80,
            temperature=0.2
        )

        print("✅ GROQ RESPONSE RECEIVED")

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("❌ GROQ ERROR:", e)
        return "AI explanation unavailable due to system error."