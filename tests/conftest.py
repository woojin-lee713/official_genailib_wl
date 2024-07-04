def pytest_configure(config):
    """
    Configure pytest with custom markers.

    This function adds a custom marker 'e2e' to pytest configuration.
    The 'e2e' marker is used to mark a test as an end-to-end test.

    Args:
        config (pytest.Config): The pytest configuration object.
    """
    config.addinivalue_line("markers", "e2e: mark a test as an end-to-end test.")
