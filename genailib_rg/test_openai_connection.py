import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Ensure the API key is set
if not openai.api_key:
    print("API key is not set.")
else:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You have the following task:"},
                      {"role": "user", "content": "Tell me a joke"}]
        )
        print(response['choices'][0]['message']['content'].strip())
    except Exception as e:
        print(f"An error occurred: {e}")
