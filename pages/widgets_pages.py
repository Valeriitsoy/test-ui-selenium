import random
import time

from loguru import logger
from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_colors, generated_date
from locators.widgets_page_locators import AccordionPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators
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


class DatePickerPage(BasePage):

    locators = DatePickerPageLocators()

    @pysnooper.snoop()
    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.select_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.select_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.select_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @pysnooper.snoop()
    def select_date_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_TIME_MONTH).click()
        self.select_date_item_from_list(self.locators.DATE_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_TIME_YEAR).click()
        self.select_date_item_from_list(self.locators.DATE_TIME_YEAR_LIST, '2021')
        self.select_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.select_date_item_from_list(self.locators.DATE_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after


class SliderPage(BasePage):

    locators = SliderPageLocators()

    @pysnooper.snoop()
    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):

    locators = ProgressBarPageLocators()

    @pysnooper.snoop()
    def change_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(1, 4))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):

    locators = TabsPageLocators()

    @pysnooper.snoop()
    def check_tabs(self, name_tab):
        tabs = {
            'what':
                {
                    'title': self.locators.TABS_WHAT,
                    'content': self.locators.TABS_WHAT_CONTENT
                 },
            'origin':
                {
                    'title': self.locators.TABS_ORIGIN,
                    'content': self.locators.TABS_ORIGIN_CONTENT
                },
            'use':
                {
                    'title': self.locators.TABS_USE,
                    'content': self.locators.TABS_USE_CONTENT
                },
            'more':
                {
                    'title': self.locators.TABS_MORE,
                    'content': self.locators.TABS_MORE_CONTENT
                }
        }
        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(content)
