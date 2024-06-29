import logging
import os

import click
import openai
from dotenv import load_dotenv
from pydantic import BaseModel

# Setting up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Set up OpenAI client with the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")
openai.api_key = api_key


class ChatResponse(BaseModel):
    text: str  # The response text from OpenAI


def get_chat_response(prompt: str = "Tell me a joke") -> ChatResponse:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )
        chat_text = response["choices"][0]["message"]["content"]
        return ChatResponse(text=chat_text)
    except openai.error.OpenAIError as e:  # Using the base OpenAIError
        logger.error("API error occurred", exc_info=True)
        message = f"API error: {str(e)}"
    except openai.error.InvalidRequestError as e:
        logger.error("Invalid request error occurred", exc_info=True)
        message = f"Invalid request: {str(e)}"
    except openai.error.AuthenticationError as e:
        logger.error("Authentication error occurred", exc_info=True)
        message = f"Authentication error: {str(e)}"
    except Exception as e:
        logger.error("An unexpected error occurred", exc_info=True)
        message = f"An unexpected error occurred: {str(e)}"
    raise click.ClickException(message)


__version__ = "1.0.0"


@click.command()
@click.option(
    "--prompt",
    "-p",
    default="Tell me something interesting",
    help="Send a prompt to the OpenAI chatbot",
    metavar="PROMPT",
    show_default=True,
)
@click.version_option(version=__version__)
def main(prompt: str) -> None:
    """
    This is the console interface to the 'get_chat_response' function.
    It interacts with OpenAI to get responses based on your prompt.
    """
    try:
        response = get_chat_response(prompt=prompt)
        click.secho(response.text, fg="green")
    except Exception as e:
        click.secho("Failed to fetch response: " + str(e), fg="red")


if __name__ == "__main__":
    main()
