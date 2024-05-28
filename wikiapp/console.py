import textwrap

import click

from wikiapp import __version__
from wikiapp.wikipedia import random_page


@click.command()
@click.option(
    "--language",
    "-1",
    default="en",
    help="gets random page from wikipedia in given language",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language):
    """The ultramodern Python project."""
    data = random_page(language=language)
    title = data["title"]
    extract = data["extract"]
    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))


if __name__ == "__main__":
    main()
