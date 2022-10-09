from pages.interactions_page import SortablePage, SelectablePage


class TestInteractions:

    class TestSortable:

        def test_sortable(self, driver):
            sort_ = SortablePage(driver, 'https://demoqa.com/sortable')
            sort_.open()
            list_before, list_after = sort_.change_list_order()
            grid_before, grid_after = sort_.change_grid_order()
            assert list_before != list_after, "Order of list not changed"
            assert grid_before != grid_after, "Order of list not changed"

    class TestSelectable:

        def test_selectable(self, driver):
            select_ = SelectablePage(driver, 'https://demoqa.com/selectable')
            select_.open()
            list_ = select_.select_list_item()
            grid_ = select_.select_grid_item()
            assert len(list_) > 0, "No selected elements"
            assert len(grid_) > 0, "No selected elements"
