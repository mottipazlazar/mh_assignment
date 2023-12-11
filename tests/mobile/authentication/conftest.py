import pytest
from infra.components.assertions.login_assertions import LoginAssertions


@pytest.fixture(scope="module")
def login_assertion(mobile) -> LoginAssertions:
    """
    Fixture providing an instance of LoginAssertions for login-related assertions.
    """
    yield LoginAssertions(mobile)
