import os
from unittest.mock import MagicMock, patch

import openai
import pytest
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


@patch("openai.chat.completions.create")
def test_chat_response_success(mock_create: MagicMock) -> None:
    """
    Test a successful response from OpenAI API.

    Args:
        mock_create (MagicMock): The mocked 'openai.chat.completions.create' function.
    """
    # Mock response
    mock_response = MagicMock()
    mock_response.choices[0].message.content = (
        "Why did the scarecrow win an award? Because he was "
        "outstanding in his field!"
    )
    mock_create.return_value = mock_response

    # Ensure the API key is set
    assert openai.api_key == os.getenv("OPENAI_API_KEY")

    # Run the actual code
    try:
        response = openai.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me a joke"},
            ],
            model="gpt-3.5-turbo",
        )
        joke = response.choices[0].message.content

        # Check if the mock response is used
        assert joke == (
            "Why did the scarecrow win an award? Because he was "
            "outstanding in his field!"
        )
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")


@patch("openai.chat.completions.create")
def test_chat_response_fail(mock_create: MagicMock) -> None:
    """
    Test a failed response from OpenAI API.

    Args:
        mock_create (MagicMock): The mocked 'openai.chat.completions.create' function.
    """
    # Mock response to raise an exception
    mock_create.side_effect = Exception("API request failed")

    # Ensure the API key is set
    assert openai.api_key == os.getenv("OPENAI_API_KEY")

    # Run the actual code and expect it to fail
    with pytest.raises(Exception) as e:
        openai.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me a joke"},
            ],
            model="gpt-3.5-turbo",
        )
    assert str(e.value) == "API request failed"


@patch("openai.chat.completions.create")
def test_chat_response_model(mock_create: MagicMock) -> None:
    """
    Test if the correct model is being used in the OpenAI API call.

    Args:
        mock_create (MagicMock): The mocked 'openai.chat.completions.create' function.
    """
    # Mock response
    mock_response = MagicMock()
    mock_response.choices[0].message.content = (
        "Why did the scarecrow win an award? Because he was "
        "outstanding in his field!"
    )
    mock_create.return_value = mock_response

    # Ensure the API key is set
    assert openai.api_key == os.getenv("OPENAI_API_KEY")

    # Run the actual code
    try:
        response = openai.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me a joke"},
            ],
            model="gpt-3.5-turbo",
        )
        joke = response.choices[0].message.content

        # Check if the correct model is being used
        mock_create.assert_called_with(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me a joke"},
            ],
            model="gpt-3.5-turbo",
        )
        assert joke == (
            "Why did the scarecrow win an award? Because he was "
            "outstanding in his field!"
        )
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")


@pytest.mark.e2e
def test_chat_response_e2e_success() -> None:
    """
    End-to-end test for a successful response from OpenAI API.
    """
    if not openai.api_key:
        pytest.fail("API key is not set. Please check your .env file.")
    else:
        try:
            response = openai.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Tell me a joke"},
                ],
                model="gpt-3.5-turbo",
            )
            joke = response.choices[0].message.content
            print("Joke:", joke)

            # Add an assertion for the joke content to ensure it is a string
            assert isinstance(joke, str) and len(joke) > 0
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")


@pytest.mark.e2e
def test_chat_response_e2e_fail() -> None:
    """
    End-to-end test for a failed response from OpenAI API.
    """
    if not openai.api_key:
        pytest.fail("API key is not set. Please check your .env file.")
    else:
        try:
            with patch(
                "openai.chat.completions.create",
                side_effect=Exception("API request failed"),
            ):
                openai.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": "Tell me a joke"},
                    ],
                    model="gpt-3.5-turbo",
                )
        except Exception as e:
            assert str(e) == "API request failed"


# Tests with gpt-4-turbo
@patch("openai.chat.completions.create")
def test_chat_response_success2(mock_create: MagicMock) -> None:
    """
    Test a successful response from OpenAI API with gpt-4-turbo model.

    Args:
        mock_create (MagicMock): The mocked 'openai.chat.completions.create' function.
    """
    # Mock response
    mock_response = MagicMock()
    mock_response.choices[0].message.content = (
        "Why did the scarecrow win an award? Because he was "
        "outstanding in his field!"
    )
    mock_create.return_value = mock_response

    # Ensure the API key is set
    assert openai.api_key == os.getenv("OPENAI_API_KEY")

    # Run the actual code
    try:
        response = openai.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me a joke"},
            ],
            model="gpt-4-turbo",
        )
        joke = response.choices[0].message.content

        # Check if the mock response is used
        assert joke == (
            "Why did the scarecrow win an award? Because he was "
            "outstanding in his field!"
        )
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")


@patch("openai.chat.completions.create")
def test_chat_response_fail2(mock_create: MagicMock) -> None:
    """
    Test a failed response from OpenAI API with gpt-4-turbo model.

    Args:
        mock_create (MagicMock): The mocked 'openai.chat.completions.create' function.
    """
    # Mock response to raise an exception
    mock_create.side_effect = Exception("API request failed")

    # Ensure the API key is set
    assert openai.api_key == os.getenv("OPENAI_API_KEY")

    # Run the actual code and expect it to fail
    with pytest.raises(Exception) as e:
        openai.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me a joke"},
            ],
            model="gpt-4-turbo",
        )
    assert str(e.value) == "API request failed"


@patch("openai.chat.completions.create")
def test_chat_response_model2(mock_create: MagicMock) -> None:
    """
    Test if the correct model is being used in the
    OpenAI API call with gpt-4-turbo model.

    Args:
        mock_create (MagicMock): The mocked 'openai.chat.completions.create' function.
    """
    # Mock response
    mock_response = MagicMock()
    mock_response.choices[0].message.content = (
        "Why did the scarecrow win an award? Because he was "
        "outstanding in his field!"
    )
    mock_create.return_value = mock_response

    # Ensure the API key is set
    assert openai.api_key == os.getenv("OPENAI_API_KEY")

    # Run the actual code
    try:
        response = openai.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me a joke"},
            ],
            model="gpt-4-turbo",
        )
        joke = response.choices[0].message.content

        # Check if the correct model is being used
        mock_create.assert_called_with(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me a joke"},
            ],
            model="gpt-4-turbo",
        )
        assert joke == (
            "Why did the scarecrow win an award? Because he was "
            "outstanding in his field!"
        )
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")


@pytest.mark.e2e
def test_chat_response_e2e_success2() -> None:
    """
    End-to-end test for a successful response from OpenAI API with gpt-4-turbo model.
    """
    if not openai.api_key:
        pytest.fail("API key is not set. Please check your .env file.")
    else:
        try:
            response = openai.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Tell me a joke"},
                ],
                model="gpt-4-turbo",
            )
            joke = response.choices[0].message.content
            print("Joke:", joke)

            # Add an assertion for the joke content to ensure it is a string
            assert isinstance(joke, str) and len(joke) > 0
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")


@pytest.mark.e2e
def test_chat_response_e2e_fail2() -> None:
    """
    End-to-end test for a failed response from OpenAI API with gpt-4-turbo model.
    """
    if not openai.api_key:
        pytest.fail("API key is not set. Please check your .env file.")
    else:
        try:
            with patch(
                "openai.chat.completions.create",
                side_effect=Exception("API request failed"),
            ):
                openai.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": "Tell me a joke"},
                    ],
                    model="gpt-4-turbo",
                )
        except Exception as e:
            assert str(e) == "API request failed"


if __name__ == "__main__":
    pytest.main()
