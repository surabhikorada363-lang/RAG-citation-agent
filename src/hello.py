import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()
client = genai.Client()

# Tried in order. Edit this list if AI Studio shows different names.
MODELS = [
    "gemini-3.5-flash-lite",
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-3.7-flash",
]

def ask(prompt, retries_per_model=2):
    for model in MODELS:
        for attempt in range(retries_per_model):
            try:
                resp = client.models.generate_content(model=model, contents=prompt)
                print(f"(answered by {model})")
                return resp.text
            except errors.ClientError as e:
                print(f"{model}: client error {e.code} (wrong name, or rate limit). Trying next model...")
                break
            except errors.ServerError as e:
                wait = 2 ** attempt
                print(f"{model}: server busy ({e.code}). Retrying in {wait}s...")
                time.sleep(wait)
    raise RuntimeError("All models failed. Try again in a few minutes.")

print(ask("Explain RAG in two sentences."))