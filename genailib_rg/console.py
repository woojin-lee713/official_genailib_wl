#import textwrap

#import click

#from genailib_rg import __version__
#from wikiapp.wikipedia import random_page


#@click.command()
#@click.option(
    #"--language",
    #"-1",
    #default="en",
    #help="gets random page from wikipedia in given language",
    #metavar="LANG",
    #show_default=True,
#)
#@click.version_option(version=__version__)
#def main(
    #language: str,  # The language you want to use is a two character string
#) -> None:  # This is a console function so returns nothing
    #"""
    #This is the console interface to 'random_page' function in wikipedia.py

   # it comes in cool colors
    #"""
    #page = random_page(language=language)
    #title = page.title
    #extract = page.extract
    #click.secho(title, fg="green")
    #click.echo(textwrap.fill(extract))


#if __name__ == "__main__":
   # main()
import os
from dotenv import load_dotenv
import textwrap
import click
from genailib_rg import __version__, get_chat_response

load_dotenv()  # This loads the environment variables from the .env file

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
