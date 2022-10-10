from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage


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

    class TestDroppable:

        def test_simple_droppable(self, driver):
            drop_ = DroppablePage(driver, 'https://demoqa.com/droppable')
            drop_.open()
            text_ = drop_.drop_simple()
            assert text_ == 'Dropped!', "Element not dropped"

        def test_accept_droppable(self, driver):
            drop_ = DroppablePage(driver, 'https://demoqa.com/droppable')
            drop_.open()
            text_not_accept, text_accept = drop_.drop_accept()
            assert text_not_accept == 'Drop here', "Element not accept"
            assert text_accept == 'Dropped!', "Element accept"

        def test_prevent_propogation_droppable(self, driver):
            drop_ = DroppablePage(driver, 'https://demoqa.com/droppable')
            drop_.open()
            text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, \
                text_greedy_inner_box = drop_.drop_prevent_propogation()
            assert text_not_greedy_box == 'Dropped!'
            assert text_not_greedy_inner_box == 'Dropped!'
            assert text_greedy_box == 'Outer droppable'
            assert text_greedy_inner_box == 'Dropped!'

        def test_revert_draggable_droppable(self, driver):
            drop_ = DroppablePage(driver, 'https://demoqa.com/droppable')
            drop_.open()
            will_after_move, will_after_revert = drop_.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = drop_.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert
            assert not_will_after_move == not_will_after_revert

    class TestDragabble:

        def test_simple_draggable(self, driver):
            drag_ = DragabblePage(driver, 'https://demoqa.com/dragabble')
            drag_.open()
            before_, after_ = drag_.simple_dragabble_box()
            assert before_ != after_, "Position not changed"

        def test_axis_restricted_draggable(self, driver):
            drag_ = DragabblePage(driver, 'https://demoqa.com/dragabble')
            drag_.open()
            top_x, left_x = drag_.axis_restricted_x()
            top_y, left_y = drag_.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0
            assert top_y[0][0] != top_x[1][0] and int(top_y[1][0]) != 0
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0


