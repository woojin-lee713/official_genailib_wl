from unittest.mock import Mock

import pytest
import requests
from click.testing import CliRunner
from pytest_mock import MockFixture

from wikiapp import console


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    return mocker.patch("wikiapp.wikipedia.random_page")


# def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
# runner.invoke(console.main, ["--language", "es"])
# print(">>>", mock_wikipedia_random_page.call_args)
# mock_wikipedia_random_page.assert_called_with(language="en")


def test_main_prints_title(runner: CliRunner, mock_requests_get: Mock) -> None:
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_invokes_requests_get(runner: CliRunner, mock_requests_get: Mock) -> None:
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_correct_url(runner: CliRunner, mock_requests_get: Mock) -> None:
    runner.invoke(console.main)
    assert mock_requests_get.call_args[0] == (
        "https://en.wikipedia.org/api/rest_v1/page/random/summary",
    )


def test_main_fail_on_request_error(runner: CliRunner, mock_requests_get: Mock) -> None:
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_print_message_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


@pytest.mark.e2e
def test_main_succeeds(runner: CliRunner) -> None:
    result = runner.invoke(console.main)
    print(">>>", result.output)
    assert result.exit_code == 0
