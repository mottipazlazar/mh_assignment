from appium import webdriver
from infra.components.action_bot import ActionBot
from infra.components.entities.device_config import get_android_desired_caps
from infra.components.entities.selector import Selector
from infra.components.mobile import Mobile
from appium.webdriver.common.appiumby import AppiumBy


class AndroidMobile(Mobile):

    def __init__(self):
        super().__init__()
        self.vendor = 'android'

        # Android Selectors:
        # buttons
        self._already_a_member_login_button_s = Selector(by=AppiumBy.ID, value='log_in_textview',
                                                         description='Already_a_member_login_button')
        self._login_button_s = Selector(by=AppiumBy.ID, value='login_button', description='login_button')
        self._top_burger_menu_s = Selector(by=AppiumBy.XPATH,
                                           value='//android.widget.ImageButton[@content-desc="Open"]',
                                           description='burger_menu_button_on_landing_page')
        self._settings_menu_button_s = Selector(by=AppiumBy.ID, value='burger_menu_settings',
                                                description='burger_menu_settings')
        self._account_setting_button_s = Selector(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout'
                                                                           '/android.widget.LinearLayout/android.widget.'
                                                                           'FrameLayout/android.widget.FrameLayout'
                                                                           '/android.widget.FrameLayout/android.view.'
                                                                           'ViewGroup/android.widget.FrameLayout/'
                                                                           'android.widget.LinearLayout/android.widget.'
                                                                           'ScrollView/android.widget.LinearLayout/'
                                                                           'android.widget.LinearLayout[2]/android.'
                                                                           'widget.TextView',
                                                  description='account_setting_button')
        self._logout_account_button_s = Selector(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/'
                                                                          'android.widget.LinearLayout/android.widget.'
                                                                          'FrameLayout/android.widget.FrameLayout/'
                                                                          'android.widget.FrameLayout/android.view.'
                                                                          'ViewGroup/android.widget.FrameLayout/android'
                                                                          '.widget.LinearLayout/android.widget.'
                                                                          'LinearLayout[1]/android.widget.TextView',
                                                 description='logout_account_button')

        # popups buttons
        self._logout_popup_ok_button_s = Selector(by=AppiumBy.ID, value='positive_horizontal_btn',
                                                  description='logout_popup_ok_button')
        self._failed_login_ok_button_s = Selector(by=AppiumBy.ID, value='positive_horizontal_btn',
                                                  description='failed_login_ok_button')

        # text fields
        self._login_email_text_s = Selector(by=AppiumBy.ID, value='email_edit_text',
                                            description='login_email_text_field')
        self._login_password_text_s = Selector(by=AppiumBy.ID, value='password_edit_text',
                                               description='login_passw_text_field')

    def init(self):
        self.desired_caps = get_android_desired_caps(self)
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

    # below are few buttons needed to be clicked on the logout flow. I've addded them here although POM is much better
    def click_top_burger_menu(self):
        self._bot.click(self._top_burger_menu_s)

    def click_settings_menu_button(self):
        self._bot.click(self._settings_menu_button_s)

    def click_account_setting_button(self):
        self._bot.click(self._account_setting_button_s)

    def click_logout_button(self):
        self._bot.click(self._logout_account_button_s)

    def approve_logout_popup_ok_button(self):
        self._bot.click(self._logout_popup_ok_button_s)

    def approve_failed_login_ok_button(self):
        self._bot.click(self._failed_login_ok_button_s)
