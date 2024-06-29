import click
from dotenv import load_dotenv

from genailib_rg.genailib_rg_sub import __version__, get_chat_response

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
