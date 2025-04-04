from google import genai
client = genai.Client(api_key="Gemini_Api_Key")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works"
)
print(response.text)