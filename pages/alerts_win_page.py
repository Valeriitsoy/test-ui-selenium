import random
import time

from loguru import logger
import pysnooper
from selenium.common import UnexpectedAlertPresentException

from locators.alert_win_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage

logger.add("debug.log", format="{time} {level} {message}")


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def check_opened_new(self, value):
        if value == 'tab':
            self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
            self.switch_to_new_window_get_url()
            text_ = self.element_is_present(self.locators.TITLE_NEW).text
            logger.info(text_)
            return text_

        if value == 'win':
            self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
            self.switch_to_new_window_get_url()
            text_ = self.element_is_present(self.locators.TITLE_NEW).text
            logger.info(text_)
            return text_

    @pysnooper.snoop()
    def check_opened_new_win_message(self):
        self.element_is_visible(self.locators.NEW_WINDOW_MESSAGE_BUTTON).click()
        self.driver.switch_to.new_window()
        text_ = self.element_is_present(self.locators.TEXT_NEW).text
        logger.info(text_)
        return text_


class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    @pysnooper.snoop()
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        return self.get_text_from_alert()

    @pysnooper.snoop()
    def check_five_seconds_alert(self):
        self.element_is_visible(self.locators.ALERT_FIVE_SECONDS_BUTTON).click()
        time.sleep(5)
        return self.get_text_from_alert()

    @pysnooper.snoop()
    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_BUTTON).click()
        time.sleep(2)
        self.accept_alert()
        return self.element_is_present(self.locators.CONFIRM_RESULT_TEXT).text

    @pysnooper.snoop()
    def check_dismiss_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_BUTTON).click()
        time.sleep(2)
        self.dismiss_alert()
        return self.element_is_present(self.locators.CONFIRM_RESULT_TEXT).text

    @pysnooper.snoop()
    def check_prompt_alert(self):
        text_ = f'TEST {random.randint(1, 999)}'
        self.element_is_visible(self.locators.PROMPT_BOX_BUTTON).click()
        self.prompt_alert(text_)
        time.sleep(2)
        self.accept_alert()
        return text_, self.element_is_present(self.locators.PROMPT_RESULT_TEXT).text


