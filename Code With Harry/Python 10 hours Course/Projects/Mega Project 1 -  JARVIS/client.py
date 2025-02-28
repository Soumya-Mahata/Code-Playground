from openai import OpenAI
client = OpenAI(api_key="OpenAI_API_KEY",)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like opening websites, playing music, and fetching news."},
        {
            "role": "user",
            "content": "What is coding?"
        }
    ]
)

print(completion.choices[0].message['content'])