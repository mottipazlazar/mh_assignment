from appium.webdriver import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.components.entities.selector import Selector
from infra.drivers.report.report_manager import ReportManager


class ActionBot:
    """
    A utility class for performing common actions on mobile applications using Appium.

    Attributes:
        __driver (webdriver): The Appium WebDriver instance.
        __report (ReportManager): An instance of the ReportManager for logging.

    Methods:
        click(selector: Selector, timeout: int = 3)
            Perform a click/tap action on an element identified by the given selector.

        clear_field_and_type_text(text_field_s: Selector, text: str, vendor: str)
            Clear a text field and type the specified text.

        clear_text_field(selector: Selector)
            Clear the text from a text field identified by the given selector.

        type_text(selector: Selector, text: str, vendor: str)
            Type the specified text into a text field identified by the given selector.

        is_element_exist(selector: Selector) -> bool
            Check if an element identified by the given selector exists.

        close_android_keyboard_if_opened()
            Close the Android keyboard if it is currently open.

        is_alert_displayed(timeout_in_sec=2) -> bool
            Check if an alert is displayed within the specified timeout.

    """
    def __init__(self, driver: webdriver):
        self.__driver: webdriver = driver
        self.__report = ReportManager()

    def click(self, selector: Selector, timeout: int = 3):
        self.__report_action_on_element('tap', selector)
        wait = WebDriverWait(self.__driver, timeout)
        element = wait.until(EC.presence_of_element_located((selector.by, selector.value)))
        element.click()

    def clear_field_and_type_text(self, text_field_s: Selector, text: str, vendor: str):
        self.clear_text_field(text_field_s)
        self.type_text(text_field_s, text, vendor)

    def clear_text_field(self, selector: Selector):
        self.__report_action_on_element('Clear Text', selector)
        element = self.__driver.find_element(selector.by, selector.value)
        element.clear()

    def type_text(self, selector: Selector, text: str, vendor):
        self.__report_action_on_element('Type Text', selector)
        element = self.__driver.find_element(selector.by, selector.value)
        element.send_keys(text)
        self.__report_message(f"--> {selector.description}: {text}")
        # check if keyboard is opened and close it
        if vendor == 'ios':
            keyboard_done_s = Selector(by=AppiumBy.ACCESSIBILITY_ID, value='Done', description='keyboard Done button')
            if self.is_element_exist(keyboard_done_s):
                self.__driver.find_element(keyboard_done_s.by, keyboard_done_s.value).click()
        elif vendor == 'android':
            self.close_android_keyboard_if_opened()

    def is_element_exist(self, selector: Selector) -> bool:
        if self.__driver.find_elements(selector.by, selector.value):
            return True
        else:
            return False

    def close_android_keyboard_if_opened(self):
        if self.__driver.is_keyboard_shown():
            self.__driver.hide_keyboard()


    def is_alert_displayed(self, timeout_in_sec=2) -> bool:
        try:
            self.__report_message(f"MIGHT WAIT UP TO {timeout_in_sec}s ON is_alert_displayed")
            wait = WebDriverWait(self.__driver, timeout=timeout_in_sec)
            wait.until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False

    # report methods:
    def __report_action_on_element(self, action: str, selector: Selector):
        self.__report.debug(f"## ACTION: {action} ~~ ON ELEMENT: {selector.description} ##")

    def __report_message(self, message: str):
        self.__report.debug(f"## {message} ##")
