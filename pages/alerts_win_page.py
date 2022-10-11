import random
import time

import allure
from loguru import logger
import pysnooper
from locators.alert_win_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage

logger.add("debug.log", format="{time} {level} {message}")


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    @allure.step("check_opened_new")
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

    @allure.step("check_opened_new_win_message")
    def check_opened_new_win_message(self):
        self.element_is_visible(self.locators.NEW_WINDOW_MESSAGE_BUTTON).click()
        self.driver.switch_to.new_window()
        text_ = self.element_is_present(self.locators.TEXT_NEW).text
        logger.info(text_)
        return text_


class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    @allure.step("check_see_alert")
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        return self.get_text_from_alert()

    @allure.step("check_five_seconds_alert")
    def check_five_seconds_alert(self):
        self.element_is_visible(self.locators.ALERT_FIVE_SECONDS_BUTTON).click()
        time.sleep(5)
        return self.get_text_from_alert()

    @pysnooper.snoop()
    @allure.step("check_confirm_alert")
    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_BUTTON).click()
        time.sleep(2)
        self.accept_alert()
        return self.element_is_present(self.locators.CONFIRM_RESULT_TEXT).text

    @pysnooper.snoop()
    @allure.step("check_dismiss_alert")
    def check_dismiss_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_BUTTON).click()
        time.sleep(2)
        self.dismiss_alert()
        return self.element_is_present(self.locators.CONFIRM_RESULT_TEXT).text

    @pysnooper.snoop()
    @allure.step("check_prompt_alert")
    def check_prompt_alert(self):
        text_ = f'TEST {random.randint(1, 999)}'
        self.element_is_visible(self.locators.PROMPT_BOX_BUTTON).click()
        self.prompt_alert(text_)
        time.sleep(2)
        self.accept_alert()
        return text_, self.element_is_present(self.locators.PROMPT_RESULT_TEXT).text


class FramesPage(BasePage):

    locators = FramesPageLocators()

    @pysnooper.snoop()
    @allure.step("check_frame")
    def check_frame(self, frame_number):
        if frame_number == 'frame1':
            frame = self.element_is_present(self.locators.FRAME_ONE)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_number == 'frame2':
            frame = self.element_is_present(self.locators.FRAME_TWO)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]


class NestedFramesPage(BasePage):

    @pysnooper.snoop()
    @allure.step("check_nested_frame")
    def check_nested_frame(self):

        p_text = self.get_frame_text('parent')
        c_text = self.get_frame_text('child')

        return p_text, c_text


class ModalDialogsPage(BasePage):

    locators = ModalDialogsPageLocators()

    @pysnooper.snoop()
    @allure.step("check_modal_dialog")
    def check_modal_dialog(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        self.element_is_visible(self.locators.SMALL_CLOSE_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        return title_small, title_large

