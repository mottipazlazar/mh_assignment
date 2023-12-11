import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from infra.components.action_bot import ActionBot
from infra.components.entities.selector import Selector
from infra.components.mobile import Mobile
from infra.components.entities.device_config import get_ios_desired_caps
from infra.components.wda import Wda


class IosMobile(Mobile):

    def __init__(self):
        super().__init__()
        self.vendor = 'ios'

        # iOS Selectors:
        # buttons
        self._already_a_member_login_button_s = Selector(by=AppiumBy.ACCESSIBILITY_ID, value='Already a member? Log In',
                                                         description='Already_a_member_login_button')
        self._login_button_s = Selector(by=AppiumBy.ACCESSIBILITY_ID, value='signup_login_submit_button',
                                        description='login_button')
        self._top_burger_menu_s = Selector(by=AppiumBy.ACCESSIBILITY_ID, value='Home_Hamburger_Menu_Button',
                                           description='burger_menu_button_on_landing_page')
        self._settings_menu_button_s = Selector(by=AppiumBy.ACCESSIBILITY_ID,
                                                value='menu_item_arrow_button_with_type_17',
                                                description='burger_menu_settings')
        self._logout_settings_button_s = Selector(by=AppiumBy.ACCESSIBILITY_ID, value='Log Out',
                                                  description='logout_account_button')

        # popups buttons
        self._logout_popup_yes_button_s = Selector(by=AppiumBy.ACCESSIBILITY_ID, value='Yes',
                                                   description='logout_popup_yes_button')
        self._failed_login_ok_button_s = Selector(by=AppiumBy.ACCESSIBILITY_ID, value='OK',
                                                  description='failed_login_ok_button')

        # text fields
        self._login_email_text_s = Selector(by=AppiumBy.ACCESSIBILITY_ID, value='formelement_email_textfield',
                                            description='login_email_text_field')
        self._login_password_text_s = Selector(by=AppiumBy.ACCESSIBILITY_ID, value='formelement_password_textfield',
                                               description='login_passw_text_field')

    def init(self):
        self.desired_caps = get_ios_desired_caps(self)
        Wda.install_wda(self.report)
        self.report.info("Going to sleep for few seconds to finish installations and connect to WDA")
        time.sleep(5)
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        self.report.info("#######   Appium Session is UP   #######")
        self._bot: ActionBot = ActionBot(self._driver)

    # action methods  # TODO maybe consoliate mobile methods ios & android
    def click_already_a_member_login(self):
        self._bot.click(self._already_a_member_login_button_s)

    def click_login_button(self):
        self._bot.click(self._login_button_s)

    def type_email(self, email: str = ""):
        self._bot.clear_field_and_type_text(text_field_s=self._login_email_text_s, text=email, vendor=self.vendor)

    def type_password(self, password: str = ""):
        self._bot.clear_field_and_type_text(text_field_s=self._login_password_text_s, text=password, vendor=self.vendor)

    def click_top_burger_menu(self):
        self._bot.click(self._top_burger_menu_s)

    def click_settings_menu_button(self):
        self._bot.click(self._settings_menu_button_s)

    def click_account_setting_button(self):
        pass

    def click_logout_button(self):
        self._bot.click(self._logout_settings_button_s)

    def approve_logout_popup_ok_button(self):
        self._bot.click(self._logout_popup_yes_button_s)

    def approve_failed_login_ok_button(self):
        self._bot.click(self._failed_login_ok_button_s)
