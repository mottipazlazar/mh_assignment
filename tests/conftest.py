import pytest
import _pytest
import config
from infra.drivers.report.report_manager import ReportManager


@pytest.fixture(scope="session")
def report():
    """
    Fixture providing a session-scoped instance of the ReportManager for logging.

    Returns:
        ReportManager: Instance of ReportManager for logging.

    """
    return ReportManager()


def pytest_addoption(parser):
    """
    Hook to add custom command line options.

    Args:
        parser (_pytest.config.argparsing.Parser): Pytest argument parser.

    Returns:
        None

    """
    group = parser.getgroup('MyHeritage')

    def add_option(key, description):
        group.addoption(
            '--' + key,
            action='store',
            dest='dest_' + key,
            default=None,
            help=description
        )
        parser.addini(key, description)

    add_option(key='mobile_os_type', description='MyHeritage Mobile os type [ "android | "ios" ]')


def set_config(pytest_config: _pytest.config.Config):
    """
    Set configuration values based on command line options and ini file.

    Args:
        pytest_config (_pytest.config.Config): Pytest configuration.

    Returns:
        None

    """
    def read_value(key: str, default: str) -> str:
        if getattr(pytest_config.option, 'dest_' + key):
            return getattr(pytest_config.option, 'dest_' + key)
        if key in pytest_config.inicfg:
            return pytest_config.inicfg[key]
        return default

    config.mobile_os_type = read_value("mobile_os_type", config.mobile_os_type)


def pytest_sessionstart(session):
    """
    Hook called when the pytest session is started.

    Args:
        session (_pytest.main.Session): Pytest session.

    Returns:
        None

    """
    set_config(session.config)
