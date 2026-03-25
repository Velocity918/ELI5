from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("API_KEY")

def ELI5(user_request):
    


    from openrouter import OpenRouter

    client = OpenRouter(
        api_key=api_key,
        server_url="https://ai.hackclub.com/proxy/v1",
    )

    response = client.chat.send(
        model="openai/gpt-5-mini",
        messages=[
            {"role": "system", "content": "Explain the user’s question as if they are 5 years old.\n\nRules:\n1. Use very simple, everyday words.\n2. Avoid jargon; if used, explain it simply.\n3. Assume the user has zero prior knowledge.\n4. Use short sentences (10–15 words max).\n5. Break the explanation into clear, logical steps.\n6. Use at least one simple real-life analogy.\n7. Include a basic example when possible.\n8. Focus on what the concept does, not abstract definitions.\n9. Avoid unnecessary detail or advanced theory.\n10. Stay strictly on topic and keep the explanation concise."}, 
            {"role": "user", "content": user_request}
        ],
    )

    return(response.choices[0].message.content)