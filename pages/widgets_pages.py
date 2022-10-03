from loguru import logger
from selenium.common import TimeoutException
from locators.widgets_page_locators import AccordionPageLocators
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

