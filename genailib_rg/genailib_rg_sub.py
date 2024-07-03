import os

import openai
from dotenv import load_dotenv
from pydantic import BaseModel

# Load environment variables from a .env file
load_dotenv()

# Get the API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatResponse(BaseModel):
    text: str  # The response text from OpenAI


def get_chat_responses(prompt, model="gpt-3.5-turbo", max_tokens=150, temperature=0.7):
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        # Convert the response to a list of tuples
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"


__version__ = "1.35.7"

if __name__ == "__main__":
    prompt = "What is the capital of Mexico?"
    model = input("Enter the model (default: gpt-3.5-turbo): ") or "gpt-3.5-turbo"
    response = get_chat_responses(prompt, model)
    print(response)
