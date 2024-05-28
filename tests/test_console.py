import click.testing
import pytest
import requests

from wikiapp import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def mock_wikipedia_random_page(mocker):
    return mocker.patch("wikiapp.wikipedia.random_page")


# def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
# runner.invoke(console.main, ["--language", "es"])
# print(">>>", mock_wikipedia_random_page.call_args)
# mock_wikipedia_random_page.assert_called_with(language="en")


def test_main_prints_title(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_invokes_requests_get(runner, mock_requests_get):
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_correct_url(runner, mock_requests_get):
    runner.invoke(console.main)
    assert mock_requests_get.call_args[0] == (
        "https://en.wikipedia.org/api/rest_v1/page/random/summary",
    )


def test_main_fail_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_print_message_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
