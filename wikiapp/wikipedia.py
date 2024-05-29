from typing import Any

import click
import requests

from pydantic import BaseModel, ValidationError

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


class Page(BaseModel):
    title: str
    extract: str


def random_page(language: str = "en") -> Page:
    """Get a random page from Wikipedia"""
    try:
        with requests.get(API_URL.format(language=language), timeout=10) as response:
            response.raise_for_status()
            data = response.json()
            return Page(**data)
        return data
    except (requests.RequestException, ValidationError) as error:
        message = str(error)
        raise click.ClickException(message) from error
