import random
import time

from loguru import logger
from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_colors
from locators.widgets_page_locators import AccordionPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage
import pysnooper
logger.add("debug.log", format="{time} {level} {message}")


class AccordionPage(BasePage):

    locators = AccordionPageLocators()

    @pysnooper.snoop()
    def check_accordion(self, number):
        accordion = {
            'first': {
                'title': self.locators.SECTION_1,
                'content': self.locators.SECTION_1_CONTENT
            },
            'second': {
                'title': self.locators.SECTION_2,
                'content': self.locators.SECTION_2_CONTENT
            },
            'third': {
                'title': self.locators.SECTION_3,
                'content': self.locators.SECTION_3_CONTENT
            }

        }
        section_title = self.element_is_visible(accordion[number]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordion[number]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordion[number]['content']).text
        return [section_title.text, section_content]


class AutoCompletePage(BasePage):

    locators = AutoCompletePageLocators()

    @pysnooper.snoop()
    def fill_input_multi(self):
        colors_ = random.sample(next(generated_colors()).color_name, k=random.randint(2, 6))
        for color_ in colors_:
            input_multi = self.element_is_clickable(self.locators.MULTI_COMPLETE_INPUT)
            input_multi.send_keys(color_)
            input_multi.send_keys(Keys.ENTER)
        return colors_

    @pysnooper.snoop()
    def remove_value_multi(self):
        count_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_before, count_after

    @pysnooper.snoop()
    def check_color(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors_ = []
        for color in color_list:
            colors_.append(color.text)
        return colors_

    @pysnooper.snoop()
    def remove_all_value_multi(self):
        list_ = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE_ALL)
        for value in list_:
            value.click()
            break
        result_ = self.elements_are_present(self.locators.MULTI_VALUE_TEXT)
        for value_ in result_:
            return value_.get_attribute('value')

    @pysnooper.snoop()
    def fil_input_single(self):
        color = random.sample(next(generated_colors()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    @pysnooper.snoop()
    def check_single_color(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


