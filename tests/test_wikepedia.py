from unittest.mock import Mock

import pytest

from wikiapp import wikipedia


def test_random_page_uses_given_language(mock_requests_get: Mock) -> None:
    wikipedia.random_page(language="es")
    args, _ = mock_requests_get.call_args
    assert "es.wikipedia.org" in args[0]


@pytest.mark.e2e
def test_random_page_returns_dictionary_in_production() -> None:
    page = wikipedia.random_page()
    assert "title" in page
    assert "extract" in page
