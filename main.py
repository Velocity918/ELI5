from dotenv import load_dotenv
import os

user_request = input()



load_dotenv()

api_key = os.getenv("API_KEY")
print(api_key)


print(user_request)