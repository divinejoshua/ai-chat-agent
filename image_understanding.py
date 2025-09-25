from google import genai
from decouple import config
from google.genai import types

import requests

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=config("GEMINI_API_KEY"))


image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

prompt = "What is this image?"


response = client.models.generate_content_stream(
    model="gemini-2.5-flash", 
    contents=[image, prompt])

for chunk in response:
    print(chunk.text, end="")