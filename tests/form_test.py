import time

import allure
from loguru import logger

from pages.form_page import FormPage

logger.add("debug.log", format="{time} {level} {message}")


@allure.suite("TestForm")
class TestForm:

    @allure.feature("FormPage")
    class TestFormPage:

        @allure.title("test_form")
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person = form_page.fill_form_fields()
            result = form_page.get_result_form()
            assert [person.firstname + " " + person.lastname, person.email] == [result[0], result[1]]


