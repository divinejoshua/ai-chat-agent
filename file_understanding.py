from google import genai
from decouple import config
import io
import httpx

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=config("GEMINI_API_KEY"))


# File Implementation
document_url = "https://arxiv.org/pdf/2312.11805"

# Retrieve and upload both PDFs using the File API
doc_data = io.BytesIO(httpx.get(document_url).content)

sample_pdf = client.files.upload(
  file=doc_data,
  config=dict(mime_type='application/pdf')
)


prompt = "Explain gemini and step 5.1.4.1 Machine Translation"


response = client.models.generate_content_stream(
    model="gemini-2.5-flash", 
    contents=[sample_pdf, prompt])

for chunk in response:
    print(chunk.text, end="")