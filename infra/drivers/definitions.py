import os
import subprocess

# file for keeping run definitions

# find workspace root dir
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace('/infra/drivers', "")  # This is ProjectRoot


# method for finding utility path dynamically, for example the path to ios-deploy
def find_utility_path(utility_name: str) -> str:
    """
    Find the path to a utility dynamically.

    Args:
        utility_name (str): The name of the utility to find.

    Returns:
        str: The path to the utility.

    Raises:
        Exception: If the utility is not found.

    """
    command = ["which", utility_name]
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as result:
        stdout, stderr = result.communicate()

    if result.returncode == 0:
        path = stdout.decode().strip()
        return path
    else:
        error_message = stderr.decode().strip()
        raise Exception(f"Utility '{utility_name}' not found. Error: {error_message}")
