from pages.widgets_pages import AccordionPage


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


