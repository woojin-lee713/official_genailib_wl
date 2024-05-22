import click
from wikiapp import __version__
import requests
import textwrap

from wikiapp.wikipedia import API_URL, random_page

@click.command()
@click.version_option(version=__version__)
def main():
    """The ultramodern Python project."""
    data = random_page()
    title = data["title"]
    extract = data["extract"]
    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))


if __name__=="__main__":
    main()
