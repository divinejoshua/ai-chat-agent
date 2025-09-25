from google import genai
from decouple import config
from google.genai import types

client = genai.Client(api_key=config("GEMINI_API_KEY"))

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

prompt = "Who won the euro 2024?"


response = client.models.generate_content_stream(
    model="gemini-2.5-flash", 
    contents=prompt,
    config=config
    )

for chunk in response:
    print(chunk.text, end="")