from google import genai
from decouple import config
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=config("GEMINI_API_KEY"))

response = client.models.generate_content_stream(
    model="gemini-2.5-flash", contents="Explain how AI works in few paragraphs"
)

for chunk in response:
    print(chunk.text, end="")