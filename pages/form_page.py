import os

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):

    locators = FormPageLocators()

    @allure.step("fill_form_fields")
    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(person.subject)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.PICTURE).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person

    @allure.step("get_result_form")
    def get_result_form(self):
        result_ = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for i in result_:
            self.go_to_element(i)
            data.append(i.text)
        return data


