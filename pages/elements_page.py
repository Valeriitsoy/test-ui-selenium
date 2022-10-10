import base64
import os
import random
import time

import allure
import requests
from loguru import logger
from selenium.common import TimeoutException

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsLocators, LinksLocators, UploadDownloadFilePageLocators, DynamicPropertiesLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

logger.add("debug.log", format="{time} {level} {message}")


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step("fill_all_fields")
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
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
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
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
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
        person_list = self.elements_are_present(self.locators.PERSON_LIST)
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
        self.remove_footer()
        for i in count:
            count_row_select = self.element_is_visible(self.locators.COUNT_ROWS)
            self.go_to_element(count_row_select)
            count_row_select.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{i}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.PERSON_LIST)
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


class LinksPage(BasePage):
    locators = LinksLocators()

    def check_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINk)
        href_link = simple_link.get_attribute('href')
        request = requests.get(href_link)
        if request.status_code == 200:
            simple_link.click()
            url = self.switch_to_new_window_get_url()
            return href_link, url
        else:
            return href_link, request.status_code

    def check_dynamic_link(self):
        dynamic_link = self.element_is_visible(self.locators.DYNAMIC_LINK)
        href_link = dynamic_link.get_attribute('href')
        request = requests.get(href_link)
        if request.status_code == 200:
            dynamic_link.click()
            url = self.switch_to_new_window_get_url()
            return href_link, url
        else:
            return href_link, request.status_code

    def check_api_call_link(self, url):
        r = requests.get(url)
        dict_codes = {
            201: self.locators.CREATED_LINK,
            204: self.locators.NO_CONTENT_LINK,
            301: self.locators.MOVED_LINK,
            400: self.locators.BAD_REQUEST_LINK,
            401: self.locators.UNAUTHORIZED_LINK,
            403: self.locators.FORBIDDEN_LINK,
            404: self.locators.NOT_FOUND_LINK
        }
        if r.status_code in dict_codes:
            locator_ = dict_codes.get(r.status_code)
            self.element_is_visible(locator_).click()
            time.sleep(1)
            link_response_text = self.element_is_visible((By.XPATH, "//*[@id='linkResponse']/b[1]")).text
            return r.status_code, int(link_response_text)
        else:
            return r.status_code, url


class UploadDownloadFilePage(BasePage):

    locators = UploadDownloadFilePageLocators()

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        time.sleep(2)
        check_text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        upload_name_file = file_name.split('\\')[-1]
        uploaded_name_file = check_text.split('\\')[-1]
        logger.info(upload_name_file)
        logger.info(uploaded_name_file)
        return upload_name_file, uploaded_name_file

    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        b_link = base64.b64decode(link)
        logger.info(b_link)
        path_file = rf'C:\MyPython\QA\filetest{random.randint(0, 99)}.jpeg'
        with open(path_file, 'wb+') as f:
            offset = b_link.find(b'\xff\xd8')
            f.write(b_link[offset:])
            check_file = os.path.exists(path_file)
        os.remove(path_file)
        return check_file


class DynamicProperties(BasePage):

    locators = DynamicPropertiesLocators()

    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    def check_change_color_button(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def check_visible_after_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_S_BUTTON)
        except TimeoutException:
            return False
        return True

