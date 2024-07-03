import os
import sys

import click
import openai
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# Load environment variables from a .env file
load_dotenv()

# Get the API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Ensure the API key is set
if not openai.api_key:
    print("API key is not set. Please check your .env file.")
else:
    try:
        # Make a request to the OpenAI API using the correct method
        response = openai.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me a joke"},
            ],
            model="gpt-3.5-turbo",
        )
        # To Provide the Command Line with more details
        # about whether or not the connection to openai is successful
        click.secho("Connection was Successful", fg="green")
        # Print the joke
        print(response.choices[0].message.content)

    except Exception as e:
        # Handle any potential errors
        click.secho("Connection Failed", fg="red")
        print(f"An error occurred: {e}")
