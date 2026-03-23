from dotenv import load_dotenv
import os

user_request = input()



load_dotenv()

api_key = os.getenv("API_KEY")


from openrouter import OpenRouter

client = OpenRouter(
    api_key=api_key,
    server_url="https://ai.hackclub.com/proxy/v1",
)

response = client.chat.send(
    model="openai/gpt-5-mini",
    messages=[
        {"role": "user", "content": user_request}
    ],
)

print(response.choices[0].message.content)