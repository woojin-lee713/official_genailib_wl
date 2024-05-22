import click.testing
import pytest
import requests

@pytest.fixture
def runner():
    return click.testing.CliRunner()


from wikiapp import console

def test_main_prints_title(runner,mock_requests_get):
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output

def test_main_invokes_requests_get(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert mock_requests_get.called

def test_main_uses_correct_url(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert mock_requests_get.call_args[0] == ("https://en.wikipedia.org/api/rest_v1/page/random/summary",)

def test_main_fail_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect =Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1

def test_main_print_message_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException
    result =runner.invoke(console.main)
    assert "Error" in result.output


def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
