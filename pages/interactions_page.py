import random

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from pages.base_page import BasePage
import pysnooper


class SortablePage(BasePage):

    locators = SortablePageLocators()

    @pysnooper.snoop()
    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [i.text for i in item_list]

    @pysnooper.snoop()
    def change_list_order(self):
        self.element_is_visible(self.locators.LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        return order_before, order_after

    @pysnooper.snoop()
    def change_grid_order(self):
        self.element_is_visible(self.locators.GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):

    locators = SelectablePageLocators()

    @pysnooper.snoop()
    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    @pysnooper.snoop()
    def select_list_item(self):
        self.element_is_visible(self.locators.LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    @pysnooper.snoop()
    def select_grid_item(self):
        self.element_is_visible(self.locators.GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text
