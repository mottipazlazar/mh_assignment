import subprocess

# a file to hold connected device configuration, in order later to be able to contorl OS versions' specific diffrerences
# for example: different text on permissions popups buttons
from infra.drivers.definitions import find_utility_path

ios_real_devices = {
    "00008101-001A79D114B9003A": {
        "deviceName": "QAMobile7",
        "platformName": "iOS",
        "platformVersion": "17.1",
        "udid": "00008101-001A79D114B9003A"
    }
}


android_real_devices = {
    "28231JEGR34946": {
        "deviceName": "Android",
        "udid": "28231JEGR34946"
    }

}


def get_android_device_by_udid(udid: str):
    """
    :param udid: device udid
    :return: udid from real devices list, after checking it exists
    """
    if udid in android_real_devices:
        return android_real_devices[udid]
    else:
        raise Exception(f"Device udid {udid} was not found under tests/device_config/android_real_devices list")


def get_ios_device_by_udid(udid: str):
    """
    :param udid: device udid
    :return: udid from real devices list, after checking it exists
    """
    if udid in ios_real_devices:
        return ios_real_devices[udid]
    else:
        raise Exception(f"Device udid {udid} was not found under tests/device_config/ios_real_devices list")


def get_android_desired_caps(mobile) -> dict:
    """
    define all desired_caps and return it
    """
    list_devices_command = r"adb devices"
    mobile.report.info("Going to get list of connected Android devices via USB")
    list_devices_command_stdout = subprocess.Popen(f"{list_devices_command}",
                                                   shell=True, stdout=subprocess.PIPE).stdout.read()
    connected_devices_list = list_devices_command_stdout.decode('utf-8').splitlines()[1:-1]
    num_connected_devices = len(connected_devices_list)

    if num_connected_devices == 0:
        raise Exception(
            "No Android USB-connected devices were discovered, EXITING AndroidMobile.init()")
    elif num_connected_devices > 1:
        raise Exception(
            "2 or More Android USB-connected devices were discovered. This is not supported yet. EXITING AndroidMobile.init()")
    else:
        udid = connected_devices_list[0].split('\t')[0]
        device_caps = get_android_device_by_udid(udid)
        desired_caps = dict(
            platformName="Android",
            deviceName=device_caps['deviceName'],
            appPackage="air.com.myheritage.mobile",
            appWaitActivity='.authentication.activities.AuthenticationActivity',
            automationName="UiAutomator2",
            udid=device_caps['udid'],
            noReset=True,
            ignoreHiddenApiPolicyError=True
        )
    return desired_caps


def get_ios_desired_caps(mobile) -> dict:
    """
    define all desired_caps and return it
    """
    idevice_id_path = find_utility_path('idevice_id')
    list_devices_command = rf"{idevice_id_path} -l"
    mobile.report.info("Going to get list of connected iOS devices via USB")
    list_devices_command_stdout = subprocess.Popen(f"{list_devices_command}",
                                                   shell=True, stdout=subprocess.PIPE).stdout.read()
    connected_devices_udid_list = list_devices_command_stdout.decode('utf-8').splitlines()
    num_connected_devices = len(connected_devices_udid_list)
    mobile.report.info(f"Found {num_connected_devices} connected iOS devices via USB")
    if num_connected_devices == 0:
        raise Exception(
            "No iOS USB-connected devices were discovered, EXISTING IosMobile.init()")
    elif num_connected_devices > 1:
        raise Exception(
            "2 or More iOS USB-connected devices were discovered. This is not supported yet. EXISTING IosMobile.init()")
    else:
        udid = connected_devices_udid_list[0]
        device_caps = get_ios_device_by_udid(udid)
        desired_caps = dict(
            platformName=device_caps['platformName'],
            platformVersion=device_caps['platformVersion'],
            deviceName=device_caps['deviceName'],
            udid=device_caps['udid'],
            bundleId='"com.myheritage.mobile',
            noReset=True,
            AutoAcceptAlerts=True
        )
    return desired_caps