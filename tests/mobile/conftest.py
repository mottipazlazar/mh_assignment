import pytest
from infra.components.mobile import Mobile
from infra.components.ios_mobile import IosMobile
from infra.components.android_mobile import AndroidMobile
import config


@pytest.fixture(scope="session")
def mobile(report) -> Mobile:
    """
    Fixture providing an instance of the Mobile component based on the configured platform.
    """

    report.info("#######   STARTING mobile session FIXTURE   #######")
    # read & set config params:
    if config.mobile_os_type not in ['ios', 'android']:
        raise Exception(f"Not supported platform: {config.mobile_os_type}")
    if config.mobile_os_type == 'ios':
        mobile_comp = IosMobile()
    elif config.mobile_os_type == 'android':
        mobile_comp = AndroidMobile()
    else:
        raise Exception(f"Not supported platform: {config.mobile_os_type}")
    mobile_comp.init()

    yield mobile_comp

    # quit wd
    report.info("#######   CLOSING mobile session FIXTURE   #######")
    mobile_comp.close()


