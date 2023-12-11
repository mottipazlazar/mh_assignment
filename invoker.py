import configparser
import os
import sys
import pytest
from infra.drivers.definitions import ROOT_DIR

TEST_TO_RUN = ""
SUITE = None

# default command line params
params = [
    os.path.join(ROOT_DIR,
                 "tests",
                 TEST_TO_RUN),
    "-v",
    "--color=yes"
]


def update_pytest_conf():
    """
    Reads all the environments variables. If found environment variables with the prefix 'pytest_env_variables_prefix',
    it will remove the prefix and search in the pytest.ini configuration file for option with the same name. If found,
    it will update the value of the pytest options with the environment variable value and
    will override the pytest file content.
    """
    ci_env_variables = [key for key in os.environ.keys() if key.startswith('PYTEST_')]
    if not len(ci_env_variables):
        print("No options found that needs to be updated in 'pytest.ini'")
        return
    print(f"Found {len(ci_env_variables)} properties to update in 'pytest.ini'")
    config = configparser.ConfigParser()  # helps in updating pytest.ini
    config_file_name = os.path.join(ROOT_DIR, 'pytest.ini')
    config.read(config_file_name)

    for env_var in ci_env_variables:
        option = env_var.lstrip('PYTEST_').lower()
        if not config.has_option('pytest', option):
            print(f"Option '{option}' is not exist in 'pytest.ini'. Skipping option")
            continue
        print(f"Setting option '{option}' with value '{os.environ[env_var]}' in 'pytest.ini'")
        config['pytest'][option] = os.environ[env_var]

    with open(config_file_name, 'w') as config_file:
        config.write(config_file)
        print(f"'{config_file_name}' was updated successfully")
#
#
# if __name__ == "__main__":
#     update_pytest_conf()
#     error_code = pytest.main(params)
#     sys.exit(error_code)
