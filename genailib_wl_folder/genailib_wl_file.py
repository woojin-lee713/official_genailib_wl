import os
import openai
import click
from dotenv import load_dotenv
from pydantic import BaseModel

# Load environment variables from a .env file
load_dotenv()

# Get the API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatResponse(BaseModel):
    """
    A model to represent the response from OpenAI's chat API.

    Attributes:
        text (str): The response text from OpenAI.
    """
    text: str  # The response text from OpenAI

def get_chat_responses(prompt, model="gpt-3.5-turbo", max_tokens=150, temperature=0.7):
    """
    Get chat responses from OpenAI's API based on the provided prompt.

    Args:
        prompt (str): The input text for the chat model.
        model (str): The model to use for generating responses.
        Default is "gpt-3.5-turbo".
        max_tokens (int): The maximum number of tokens to generate. Default is 150.
        temperature (float): The sampling temperature. Default is 0.7.

    Returns:
        str: The response text from OpenAI, or an error message if the API call fails.
    """
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
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

@click.command()
@click.option(
    "--prompt",
    "-p",
    default="Tell me something interesting",
    help="Send a prompt to the OpenAI chatbot",
    metavar="PROMPT",
    show_default=True,
)
@click.option(
    "--model",
    "-m",
    default="gpt-3.5-turbo",
    help="Specify the model to use",
    metavar="MODEL",
    show_default=True,
)
def main(prompt, model):
    """
    Main function to get chat responses based on command-line arguments.
    """
    response = get_chat_responses(prompt, model)
    print(response)

# Version of the module
__version__ = "1.35.7"

if __name__ == "__main__":
    main()
