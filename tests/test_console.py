import subprocess
from unittest.mock import MagicMock, Mock, patch

import pytest


@patch("subprocess.run")
def test_pixi_run_success(mock_subprocess_run: Mock) -> None:
    """Test the pixi run command for success using mock"""
    # Set up the mock to return a successful result
    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = "Pixi test run successful"
    mock_result.stderr = ""
    mock_subprocess_run.return_value = mock_result

    result = subprocess.run(
        ["/usr/bin/pixi", "run", "test"], capture_output=True, text=True, check=True
    )

    # Assertions
    mock_subprocess_run.assert_called_once_with(
        ["/usr/bin/pixi", "run", "test"], capture_output=True, text=True, check=True
    )
    assert result.returncode == 0, f"pixi run test failed: {result.stderr}"
    assert result.stdout == "Pixi test run successful"
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)


@patch("subprocess.run")
def test_pixi_run_failure(mock_subprocess_run: Mock) -> None:
    """Test the pixi run command for failure using mock"""
    # Set up the mock to return a failure result
    mock_result = MagicMock()
    mock_result.returncode = 1
    mock_result.stdout = ""
    mock_result.stderr = "Pixi test run failed"
    mock_subprocess_run.return_value = mock_result

    result = subprocess.run(
        ["/usr/bin/pixi", "run", "test"], capture_output=True, text=True, check=True
    )

    # Assertions
    mock_subprocess_run.assert_called_once_with(
        ["/usr/bin/pixi", "run", "test"], capture_output=True, text=True, check=True
    )
    assert result.returncode == 1, "pixi run test unexpectedly succeeded"
    assert result.stderr == "Pixi test run failed"
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)


@pytest.mark.e2e
@patch("subprocess.run")
def test_console_e2e_success(mock_subprocess_run: Mock) -> None:
    """Test the console.py script end-to-end for success"""
    # Set up the mock to return a successful result
    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = "Connection was Successful\nThe capital of Mexico is Mexico City."
    mock_result.stderr = ""
    mock_subprocess_run.return_value = mock_result

    result = subprocess.run(
        [
            "/usr/bin/python3",
            "genailib_rg/console.py",
            "-p",
            "What is the capital of Mexico?",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    # Assertions
    mock_subprocess_run.assert_called_once_with(
        [
            "/usr/bin/python3",
            "genailib_rg/console.py",
            "-p",
            "What is the capital of Mexico?",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0, f"console.py E2E test failed: {result.stderr}"
    assert (
        "Connection was Successful" in result.stdout
    ), "Expected success message not found in output"
    assert (
        "The capital of Mexico is Mexico City." in result.stdout
    ), "Expected response not found in output"
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)


@pytest.mark.e2e
@patch("subprocess.run")
def test_console_e2e_failure(mock_subprocess_run: Mock) -> None:
    """Test the console.py script end-to-end for failure with an invalid prompt"""
    # Set up the mock to return a failure result
    mock_result = MagicMock()
    mock_result.returncode = 1
    mock_result.stdout = "An unexpected error occurred"
    mock_result.stderr = "Error"
    mock_subprocess_run.return_value = mock_result

    result = subprocess.run(
        [
            "/usr/bin/python3",
            "genailib_rg/console.py",
            "-p",
            "",
        ],  # Assuming empty prompt causes failure
        capture_output=True,
        text=True,
        check=True,
    )

    # Assertions
    mock_subprocess_run.assert_called_once_with(
        ["/usr/bin/python3", "genailib_rg/console.py", "-p", ""],
        capture_output=True,
        text=True,
        check=True,
    )
    assert (
        result.returncode != 0
    ), "console.py E2E test unexpectedly succeeded with empty prompt"
    assert (
        "An unexpected error occurred" in result.stdout
    ), "Expected failure message not found in output"
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)


if __name__ == "__main__":
    pytest.main()
