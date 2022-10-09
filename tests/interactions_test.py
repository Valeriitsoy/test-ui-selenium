from pages.interactions_page import SortablePage


class TestInteractions:

    class TestSortable:

        def test_sortable(self, driver):
            sort_ = SortablePage(driver, 'https://demoqa.com/sortable')
            sort_.open()
            list_before, list_after = sort_.change_list_order()
            grid_before, grid_after = sort_.change_grid_order()
            assert list_before != list_after, "Order of list not changed"
            assert grid_before != grid_after, "Order of list not changed"

