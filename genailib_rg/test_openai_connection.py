import os

import openai
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Ensure the API key is set
if not openai.api_key:
    print("API key is not set. Please check your .env file.")
else:
    try:
        # Make a request to the OpenAI API using the new method
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me a joke"},
            ],
        )
        # Print the joke
        print(response["choices"][0]["message"]["content"].strip())
    except Exception as e:
        # Handle any potential errors
        print(f"An error occurred: {e}")
