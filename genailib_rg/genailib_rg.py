#import click
#import requests
#from pydantic import BaseModel, ValidationError

#API_URL = "https://api.openai.com/v1/chat/completions"


#class Page(BaseModel):
    #"A Page Dataclass to represent the return value from wikipedia"

    #title: str  # the title of the wikipedia page
    #extract: str  # the extract of the wikipedia page


#def random_page(
    #language: str = "en",  # The language you want to use, as a two character string
#) -> Page:  # Return a Page object
#    """Get a random page from Wikipedia"""
#    try:
#        with requests.get(API_URL.format(language=language), timeout=10) as response:
#            response.raise_for_status()
#            data = response.json()
#            return Page(**data)
#        return data
#    except (requests.RequestException, ValidationError) as error:
#        message = str(error)
#        raise click.ClickException(message) from error


import openai
import click
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import logging

# Setting up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatResponse(BaseModel):
    text: str  # The response text from OpenAI

def get_chat_response(prompt: str = "Tell me a joke") -> ChatResponse:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        chat_text = response['choices'][0]['message']['content']
        return ChatResponse(text=chat_text)
    except openai.error.APIError as e:
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
