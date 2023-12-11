from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from infra.components.entities.selector import Selector
from selenium.webdriver.support import expected_conditions as EC
from infra.components import mobile


# class for holding assertions method using appium
class AppAssertionHelper:

    def __init__(self, mobile_comp: mobile):
        self.driver = mobile_comp._driver
        self.report = mobile_comp.report
        self.vendor = mobile_comp.vendor

    def assert_element_is_visible(self, selector: Selector, timeout: int = 3, message="Element should be visible"):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located((selector.by, selector.value)))
        assert element.is_displayed(), message

    def assert_alert_displayed(self, timeout_in_sec=2):
        try:
            self.report.info(f"MIGHT WAIT UP TO {timeout_in_sec}s ON is_alert_displayed")
            wait = WebDriverWait(self.driver, timeout=timeout_in_sec)
            wait.until(EC.alert_is_present())
        except TimeoutException:
            raise AssertionError(f"Alert is not displayed within the specified timeout of {timeout_in_sec} sec")

    def assert_text_displayed(self, text_selector: Selector, text: str, timeout_in_sec=2) -> bool:
        self.report(f"Wait for text to be displayed: '{text}'", text_selector)
        wait = WebDriverWait(self.driver, timeout_in_sec)
        try:
            wait.until(EC.text_to_be_present_in_element((text_selector.by, text_selector.value), text))
        except TimeoutException:
            raise AssertionError(f"Text '{text}' is not displayed within the specified timeout of {timeout_in_sec} sec")
