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
            {"role": "system", "content": "You must follow all the rules:\n"
                                        "1) You have explain what ever the user ask as if he is 5 years old\n"
                                        "2) maximum word limit 150\n"
                                        "3) Absolutely no Jargon"}, 
            {"role": "user", "content": user_request}
        ],
    )

    return(response.choices[0].message.content)