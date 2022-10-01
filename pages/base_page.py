import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains as AC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = AC(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = AC(self.driver)
        action.context_click(element)
        action.perform()

    def switch_to_new_window_get_url(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.current_url

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script(" document.getElementById('close-fixedban').remove();")

    def get_text_from_alert(self):
        return self.driver.switch_to.alert.text

    def accept_alert(self, timeout=5):
        wait(self.driver, timeout).until(EC.alert_is_present())
        return self.driver.switch_to.alert.accept()

    def dismiss_alert(self, timeout=5):
        wait(self.driver, timeout).until(EC.alert_is_present())
        return self.driver.switch_to.alert.dismiss()

    def prompt_alert(self, text, timeout=5):
        wait(self.driver, timeout).until(EC.alert_is_present())
        return self.driver.switch_to.alert.send_keys(text)
