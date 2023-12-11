import config
from infra.drivers.report.report_manager import ReportManager


class MobileFlows:
    """
    Business logic layer for mobile application flows.

    This class encapsulates the common user interactions and flows in the mobile application.

    Args:
    mobile: An instance of the Mobile component.

    Attributes:
    mobile: Instance of the Mobile component.
    __report: Report manager for logging.

    Methods:
    login(email: str, password: str) -> MobileFlows:
    Perform the login operation with the provided email and password.

    logout() -> MobileFlows:
    Perform the logout operation.

    """


    def __init__(self, mobile):
        self.mobile = mobile
        self.__report = ReportManager()

    def login(self, email: str, password: str):
        self.mobile.type_email(email)
        self.mobile.type_password(password)
        self.mobile.click_login_button()
        return self

    def logout(self):
        self.mobile.click_top_burger_menu()
        self.mobile.click_settings_menu_button()
        if config.mobile_os_type == 'andorid':
            self.mobile.click_account_setting_button()
        self.mobile.click_logout_button()
        self.mobile.approve_logout_popup_ok_button()
        return self
