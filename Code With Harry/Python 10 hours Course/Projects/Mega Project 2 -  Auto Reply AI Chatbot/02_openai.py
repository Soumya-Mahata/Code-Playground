from openai import OpenAI

client = OpenAI(api_key="OpenAI_API_KEY",)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named Soumya, who can speak Bengali, English and Hindi. You are from India and are a coder. You analyze the chat history and respond like Soumya."},
        {
            "role": "user",
            "content": "chat_history"
        }
    ]
)

print(completion.choices[0].message['content'])