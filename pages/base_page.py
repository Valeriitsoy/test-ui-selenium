import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step("open")
    def open(self):
        self.driver.get(self.url)

    @allure.step("element_is_visible")
    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    @allure.step("elements_are_visible")
    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    @allure.step("element_is_present")
    def element_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    @allure.step("elements_are_present")
    def elements_are_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    @allure.step("element_is_not_visible")
    def element_is_not_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    @allure.step("element_is_clickable")
    def element_is_clickable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    @allure.step("go_to_element")
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("action_double_click")
    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step("action_right_click")
    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    @allure.step("switch_to_new_window_get_url")
    def switch_to_new_window_get_url(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.current_url

    @allure.step("remove_footer")
    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script(" document.getElementById('close-fixedban').remove();")

    @allure.step("get_text_from_alert")
    def get_text_from_alert(self):
        return self.driver.switch_to.alert.text

    @allure.step("accept_alert")
    def accept_alert(self, timeout=5):
        Wait(self.driver, timeout).until(ec.alert_is_present())
        return self.driver.switch_to.alert.accept()

    @allure.step("dismiss_alert")
    def dismiss_alert(self, timeout=5):
        Wait(self.driver, timeout).until(ec.alert_is_present())
        return self.driver.switch_to.alert.dismiss()

    @allure.step("prompt_alert")
    def prompt_alert(self, text, timeout=5):
        Wait(self.driver, timeout).until(ec.alert_is_present())
        return self.driver.switch_to.alert.send_keys(text)

    @allure.step("get_frame_text")
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

    @allure.step("select_date_by_text")
    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    @allure.step("select_date_item_from_list")
    def select_date_item_from_list(self, elements, value):
        list_ = self.elements_are_present(elements)
        for i in list_:
            if i.text == value:
                i.click()
                break

    @allure.step("action_drag_and_drop_by_offset")
    def action_drag_and_drop_by_offset(self, element, x_, y_):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_, y_)
        action.perform()

    @allure.step("action_move_to_element")
    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @allure.step("action_drag_and_drop_to_element")
    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()


