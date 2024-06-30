from unittest.mock import Mock

import pytest
from click.testing import CliRunner
from pytest_mock import MockFixture

from genailib_rg.console import main


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def mock_get_chat_response(mocker: MockFixture) -> Mock:
    return mocker.patch(
        "genailib_rg.genailib_rg_sub.get_chat_response",
        return_value=Mock(text="Test response from OpenAI"),
    )

    def test_main_prints_response(
        runner: CliRunner, mock_get_chat_response: Mock
    ) -> None:
        result = runner.invoke(main, ["--prompt", "Tell me something interesting"])
        assert "Test response from OpenAI" in result.output


def test_main_invokes_openai_api(
    runner: CliRunner, mock_get_chat_response: Mock
) -> None:
    runner.invoke(main, ["--prompt", "Hello"])
    mock_get_chat_response.assert_called_with(prompt="Hello")


def test_main_fail_on_api_error(
    runner: CliRunner, mock_get_chat_response: Mock
) -> None:
    mock_get_chat_response.side_effect = Exception("API Failure")
    result = runner.invoke(main)
    assert result.exit_code != 0
    assert "Failed to fetch response: API Failure" in result.output


@pytest.mark.e2e
def test_main_succeeds(runner: CliRunner, mock_get_chat_response: Mock) -> None:
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Test response from OpenAI" in result.output
