from appium.webdriver.common.appiumby import AppiumBy
from infra.components.assertions.apps_assertions_helper import AppAssertionHelper
from infra.components.entities.selector import Selector


#  class for assertions related to login flow
class LoginAssertions(AppAssertionHelper):  # TODO maybe separete by ios/android

    def __init__(self, mobile_comp):
        super().__init__(mobile_comp)

        # relevant selectors
        self.wrong_credentials_message_s = Selector(by=AppiumBy.ID, value='message', description='message')

    def assert_login_successful(self):
        success_selector = ""
        if self.vendor == 'andorid':
            success_selector = Selector(by=AppiumBy.ID, value='inbox', description='inbox')
        elif self.vendor == 'ios':
            success_selector = Selector(by=AppiumBy.ACCESSIBILITY_ID, value='sg inbox icon', description='inbox')
        self.assert_element_is_visible(success_selector, message='Login failed as inbox element not found')

    def assert_wrong_credentials_popup(self):
        self.assert_alert_displayed()
        self.assert_text_displayed(text_selector=self.wrong_credentials_message_s, text='Make sure you entered your '
                                                                                        'MyHeritage email/password '
                                                                                        'combination correctly')
