from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


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

    class TestResizable:

        def test_resizable(self, driver):
            resize_ = ResizablePage(driver, 'https://demoqa.com/resizable')
            resize_.open()
            max_box, min_box = resize_.change_size_resizable_box()
            max_resize, min_resize = resize_.change_size_resizable()
            assert ('500px', '300px') == max_box
            assert ('150px', '150px') == min_box
            assert max_resize != min_resize
