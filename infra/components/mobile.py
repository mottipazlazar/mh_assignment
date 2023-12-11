from abc import abstractmethod
from infra.components.action_bot import ActionBot
from infra.components.component import Component
from appium import webdriver



class Mobile(Component):
    """
    A base class representing a mobile application component with common actions.

    Attributes:
        _driver (webdriver): The Appium WebDriver instance.
        _bot (ActionBot): An instance of the ActionBot for performing actions.
        vendor (str): The mobile platform/vendor (e.g., 'ios', 'android').
        desired_caps (dict): Desired capabilities for initializing the Appium session.
    """

    def __init__(self):
        super().__init__()
        self._driver: webdriver = None
        self._bot: ActionBot = None
        self.vendor: str = None
        self.desired_caps: dict = None


    @abstractmethod
    def init(self):
        pass

    def close(self):
        """Close the Appium session and provide a log message"""
        self._driver.quit()
        self.report.info("#######   Appium Session is CLOSED   #######")

    @abstractmethod
    def click_already_a_member_login(self):
        pass

    @abstractmethod
    def click_login_button(self):
        pass

    @abstractmethod
    def type_email(self, email):
        pass

    @abstractmethod
    def type_password(self, password):
        pass

    @abstractmethod
    def click_top_burger_menu(self):
        pass
    @abstractmethod
    def click_settings_menu_button(self):
        pass

    @abstractmethod
    def click_account_setting_button(self):
        pass

    @abstractmethod
    def click_logout_button(self):
        pass

    @abstractmethod
    def approve_logout_popup_ok_button(self):
        pass

    @abstractmethod
    def approve_failed_login_ok_button(self):
        pass