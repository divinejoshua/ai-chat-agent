from google import genai
from decouple import config
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client(api_key=config("GEMINI_API_KEY"))

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

prompt = "What are the 5 ways to get a business Idea as found on this link https://medium.com/@qevoltlimited/5-ways-to-find-the-right-business-idea-6581dc6d9de6"


response = client.models.generate_content_stream(
    model="gemini-2.5-flash", 
    contents=prompt,
   config=GenerateContentConfig(
        tools=tools,
    )
    )

for chunk in response:
    print(chunk.text, end="")