from appium.webdriver.common.appiumby import AppiumBy


class Selector:
    """
    A class representing a selector used for locating elements in Appium.

    Attributes:
        by (AppiumBy): The type of selector (e.g., AppiumBy.ID, AppiumBy.XPATH).
        value (str): The value associated with the selector.
        description (str): A brief description or purpose of the selector.

    Example:
        selector = Selector(by=AppiumBy.ID, value='element_id', description='Login button')
    """
    def __init__(self, by: AppiumBy, value: str, description: str):
        self.by = by
        self.value = value
        self.description = description

