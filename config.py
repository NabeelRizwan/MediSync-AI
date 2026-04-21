import os
from google import genai

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY not set")

client = genai.Client(api_key=GOOGLE_API_KEY)
