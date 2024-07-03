import os
import sys

import click
from dotenv import load_dotenv

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import version and the get_chat_responses function
from genailib_rg.genailib_rg_sub import __version__, get_chat_responses

# Load environment variables
load_dotenv()


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
    This is the console interface to the 'get_chat_responses' function.
    It interacts with OpenAI to get responses based on your prompt.
    """
    try:
        response = get_chat_responses(prompt=prompt)
        click.secho("Connection was Successful", fg="green")
        click.secho(response)
    except click.ClickException as e:
        click.secho(f"Failed to fetch response: {e}", fg="red")
    except Exception as e:
        click.secho(f"An unexpected error occurred: {e}", fg="red")


if __name__ == "__main__":
    main()
