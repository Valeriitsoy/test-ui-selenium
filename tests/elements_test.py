import random
import time
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTexBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            out_name, out_email, out_cur_addr, out_per_addr = text_box_page.check_filled_form()

            # print(f'{out_name}\n{out_email}\n{out_cur_addr}\n{out_per_addr}')

            assert full_name == out_name, "no match"
            assert email == out_email
            assert current_address == out_cur_addr
            assert permanent_address == out_per_addr

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()
            print(f'\n{input_checkbox}\n{output_checkbox}')
            assert input_checkbox == output_checkbox, 'checkboxes have not been selected'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button.open()
            radio_button.click_on_the_radio_button('yes')
            output_yes = radio_button.get_output_result()
            radio_button.click_on_the_radio_button('impressive')
            output_impressive = radio_button.get_output_result()
            radio_button.click_on_the_radio_button('no')
            output_no = radio_button.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            input_person = web_table_page.add_new_person()
            output_person = web_table_page.check_person()
            # time.sleep()
            print(f'{input_person}\n{output_person}')
            assert input_person in output_person

        def test_web_table_search_person(self, driver):
            table_search_person = WebTablePage(driver, 'https://demoqa.com/webtables')
            table_search_person.open()
            key_random = table_search_person.add_new_person()[random.randint(0, 5)]
            table_search_person.search_person(key_random)
            table_result = table_search_person.check_search_person()
            print(key_random)
            print(table_result)
            assert key_random in table_result, "Person not added to the table"

        def test_web_table_update_person_info(self, driver):
            web_table_person = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_person.open()
            lastname = web_table_person.add_new_person()[1]
            web_table_person.search_person(lastname)
            time.sleep(1)
            age = web_table_person.update_person_info()
            row = web_table_person.check_search_person()
            print(age)
            print(row)
            assert age in row, "Person page has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_person = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_person.open()
            email = web_table_person.add_new_person()[3]
            web_table_person.search_person(email)
            time.sleep(2)
            web_table_person.delete_person()
            text = web_table_person.check_deleted()
            assert text == "No rows found"

        #  the test is successful at the size of the browser window 750х800
        def test_web_table_change_count_rows(self, driver):
            web_table_person = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_person.open()
            count = web_table_person.select_count_rows()
            assert count == [5, 10, 20, 25, 50, 100], "The number of rows in the table has change incorrectly"




