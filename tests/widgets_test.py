
from loguru import logger

from pages.widgets_pages import AccordionPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


class TestWidgets:

    class TestAccordionPage:

        def test_accordion(self, driver):
            accordion_ = AccordionPage(driver, 'https://demoqa.com/accordian')
            accordion_.open()
            title_1, content_1 = accordion_.check_accordion('first')
            title_2, content_2 = accordion_.check_accordion('second')
            title_3, content_3 = accordion_.check_accordion('third')
            assert title_1 == "What is Lorem Ipsum?" and len(content_1) > 0
            assert title_2 == "Where does it come from?" and len(content_2) > 0
            assert title_3 == "Why do we use it?" and len(content_3) > 0

    class TestAutoCompletePage:

        def test_fil_multi_autocomplete(self, driver):
            autocomplete_ = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_.open()
            colors = autocomplete_.fill_input_multi()
            colors_result = autocomplete_.check_color()
            logger.info([colors, colors_result])
            assert colors == colors_result

        def test_remove_value_multi(self, driver):
            autocomplete_ = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_.open()
            autocomplete_.fill_input_multi()
            count_before, count_after = autocomplete_.remove_value_multi()
            logger.info([count_before, count_after])
            assert count_before > count_after

        def test_remove_all_value_multi(self, driver):
            autocomplete_ = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_.open()
            autocomplete_.fill_input_multi()
            count_after = autocomplete_.remove_all_value_multi()
            logger.info(count_after)
            assert count_after is None

        def test_single_color_autocomplete(self, driver):
            autocomplete_ = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_.open()
            color_ = autocomplete_.fil_input_single()
            result_color = autocomplete_.check_single_color()
            assert color_ == result_color

    class TestDatePickerPage:

        def test_change_date(self, driver):
            data_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            data_picker_page.open()
            value_date_before, value_date_after = data_picker_page.select_date()
            assert value_date_before != value_date_after, "The date not change"

        def test_change_date_and_time(self, driver):
            data_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            data_picker_page.open()
            value_date_before, value_date_after = data_picker_page.select_date_time()
            assert value_date_before != value_date_after, "The date and time not change"

    class TestSliderPage:

        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before_, after_ = slider.change_slider_value()
            assert before_ != after_, "Slider value not changed"

    class TestProgressBarPage:

        def test_bar(self, driver):
            bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            bar.open()
            before_, after_ = bar.change_bar_value()
            assert before_ != after_, "Progress bar value not changed"

    class TestTabsPage:

        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content = tabs.check_tabs('what')
            origin_button, origin_content = tabs.check_tabs('origin')
            use_button, use_content = tabs.check_tabs('use')
            more_button, more_content = tabs.check_tabs('more')
            assert what_button == 'What', what_content > 0
            assert use_button == 'Use', use_content > 0
            assert origin_button == 'Origin', origin_content > 0
            assert more_button == 'More', more_content > 0

    class TestToolTips:

        def test_tool_tips(self, driver):
            tips_ = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tips_.open()
            tip_text_button, tip_text_field, tip_text_contrary, tip_text_section = tips_.check_tool_tips()
            assert tip_text_button == 'You hovered over the Button'
            assert tip_text_field == 'You hovered over the text field'
            assert tip_text_contrary == 'You hovered over the Contrary'
            assert tip_text_section == 'You hovered over the 1.10.32'

    class TestMenu:

        def test_menu(self, driver):
            menu_ = MenuPage(driver, 'https://demoqa.com/menu')
            menu_.open()
            data = menu_.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3']
