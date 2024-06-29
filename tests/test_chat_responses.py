# from unittest.mock import Mock

# import pytest
# from click.exceptions import ClickException

# from genailib_rg import genailib_rg


# def test_random_page_uses_given_language(mock_requests_get: Mock) -> None:
# wikipedia.random_page(language="es")
# args, _ = mock_requests_get.call_args
# assert "es.wikipedia.org" in args[0]


# def test_random_page_returns_page_in_production() -> None:
# page = wikipedia.random_page()
# assert isinstance(page, wikipedia.Page)


# def test_random_page_handles_validation_error(mock_requests_get: Mock) -> None:
# mock_requests_get.return_value.__enter__.return_value.json.return_value = {}
# with pytest.raises(ClickException):
# wikipedia.random_page()

from unittest.mock import patch

import pytest
from click.exceptions import ClickException

from genailib_rg.genailib_rg_sub import ChatResponse, get_chat_response


def test_get_chat_response_uses_given_prompt() -> None:
    with patch("openai.ChatCompletion.create") as mock_create:
        mock_create.return_value = {
            "choices": [{"message": {"content": "Hello, world!"}}]
        }
        response = get_chat_response(prompt="Hello")
        mock_create.assert_called_once_with(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello"}]
        )
        assert isinstance(response, ChatResponse)
        assert response.text == "Hello, world!"


@pytest.mark.e2e
def test_get_chat_response_returns_response_in_production() -> None:
    with patch("openai.ChatCompletion.create") as mock_create:
        mock_create.return_value = {
            "choices": [{"message": {"content": "Hello, world!"}}]
        }
        response = get_chat_response(prompt="Tell me a joke")
        assert isinstance(response, ChatResponse)
        assert response.text == "Hello, world!"


def test_get_chat_response_handles_validation_error() -> None:
    with patch("openai.ChatCompletion.create") as mock_create:
        mock_create.side_effect = Exception("An error occurred")
        with pytest.raises(ClickException):
            get_chat_response(prompt="Fail me")
