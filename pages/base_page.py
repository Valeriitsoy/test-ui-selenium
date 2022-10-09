from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
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
        Wait(self.driver, timeout).until(ec.alert_is_present())
        return self.driver.switch_to.alert.accept()

    def dismiss_alert(self, timeout=5):
        Wait(self.driver, timeout).until(ec.alert_is_present())
        return self.driver.switch_to.alert.dismiss()

    def prompt_alert(self, text, timeout=5):
        Wait(self.driver, timeout).until(ec.alert_is_present())
        return self.driver.switch_to.alert.send_keys(text)

    def get_frame_text(self, name=''):
        if name == 'parent':
            parent_ = self.element_is_present((By.CSS_SELECTOR, "iframe[id='frame1']"))
            self.driver.switch_to.frame(parent_)
            text_ = self.element_is_present((By.CSS_SELECTOR, "body")).text
            return text_
        if name == 'child':
            child_ = self.element_is_present((By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']"))
            self.driver.switch_to.frame(child_)
            text_ = self.element_is_present((By.CSS_SELECTOR, "p")).text
            return text_

    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def select_date_item_from_list(self, elements, value):
        list_ = self.elements_are_present(elements)
        for i in list_:
            if i.text == value:
                i.click()
                break

    def action_drag_and_drop_by_offset(self, element, x_, y_):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_, y_)
        action.perform()
