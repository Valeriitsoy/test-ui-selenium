import random
import time

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        count = 19
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_BUTTON,
            'impressive': self.locators.IMPRESSIVE_BUTTON,
            'no': self.locators.NO_BUTTON
        }

        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUT_RESULT).text


class WebTablePage(BasePage):

    locators = WebTablePageLocators()

    def add_new_person(self):
        count = 1
        while True:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_FIL).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_FIL).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_FIL).send_keys(email)
            self.element_is_visible(self.locators.AGE_FIL).send_keys(age)
            self.element_is_visible(self.locators.SALARY_FIL).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_FIL).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            if count == 0:
                return [firstname, lastname, str(age), email, str(salary), department]

    def check_person(self):
        person_list = self.element_are_present(self.locators.PERSON_LIST)
        data = []
        for i in person_list:
            data.append(i.text.splitlines())
        return data

    def search_person(self, key):
        self.element_is_visible(self.locators.SEARCH_FIL).send_keys(key)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        self.element_is_visible(self.locators.AGE_FIL).clear()
        self.element_is_visible(self.locators.AGE_FIL).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.element_is_visible(self.locators.NO_ROWS_FOUND).text

    def select_count_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for i in count:
            count_row_select = self.element_is_visible(self.locators.COUNT_ROWS)
            self.go_to_element(count_row_select)
            count_row_select.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{i}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.element_are_present(self.locators.PERSON_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsLocators()

    def check_click_buttons(self, element):
        return self.element_is_present(element).text

    def double_click(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_ME))
        return self.check_click_buttons(self.locators.CHECK_DOUBLE_CLICK_ME)

    def right_click(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_ME))
        return self.check_click_buttons(self.locators.CHECK_RIGHT_CLICK_ME)

    def simple_click(self):
        self.element_is_visible(self.locators.CLICK_ME).click()
        return self.check_click_buttons(self.locators.CHECK_CLICK_ME)


