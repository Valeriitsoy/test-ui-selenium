from loguru import logger
import pysnooper

from locators.alert_win_locators import BrowserWindowsPageLocators
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



