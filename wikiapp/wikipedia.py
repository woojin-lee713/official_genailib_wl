import requests
import click

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"

def random_page(language="en"):
    """Get a random page from Wikipedia"""
    try:
        with requests.get(API_URL.format(language=language)) as response:
            response.raise_for_status()
            data = response.json()
        return data
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message) from error
