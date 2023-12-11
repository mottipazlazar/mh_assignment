import os
import subprocess
from infra.drivers.definitions import ROOT_DIR, find_utility_path


# TODO Daniel, note that for ios 17.x with Xcode 15 there's no more support for ios-deploy, so it needs fixing below:
#  possibly according to https://github.com/ios-control/ios-deploy/issues/588 or https://github.com/flutter/flutter/issues/133465

class Wda:
    """
    A utility class for installing WebDriverAgent (WDA) for iOS.

    Methods:
        install_wda(report)
            Install WebDriverAgent for iOS and provide deployment information.

    """
    @staticmethod
    def install_wda(report):
        report.info("### Going to deploy ios WDA ###")
        bundle = os.path.join(ROOT_DIR, r'infra/apps/WebDriverAgentRunner-Runner.app-copy')
        ios_deploy_path = ''
        try:
            utility_name = "ios-deploy"
            ios_deploy_path = find_utility_path(utility_name)
            print(f"Path to {utility_name} has been found: {ios_deploy_path}")
        except Exception as e:
            raise e
        deploy_command = rf"{ios_deploy_path} --justlaunch --bundle "
        with subprocess.Popen(f"{deploy_command} '{bundle}'",
                              shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as deploy_logs:
            stdout, stderr = deploy_logs.communicate()
        if deploy_logs.returncode == 0:
            command_output = stdout.decode().strip()
            print(f"Deploy WDA output: {command_output}")
        else:
            error_message = stderr.decode().strip()
            raise Exception(f"Deploy WDA FAILED. Error: {error_message}")