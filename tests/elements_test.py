import random
import time

from loguru import logger

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadDownloadFilePage, DynamicProperties

logger.add("debug.log", format="{time} {level} {message}")


class TestElements:
    class TestTexBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            out_name, out_email, out_cur_addr, out_per_addr = text_box_page.check_filled_form()
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

    class TestButtons:

        def test_double_click_me(self, driver):
            web_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            web_page.open()
            double_click_result = web_page.double_click()
            assert double_click_result == 'You have done a double click', "The double click button is not pressed"

        def test_right_click_me(self, driver):
            web_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            web_page.open()
            right_click_result = web_page.right_click()
            assert right_click_result == 'You have done a right click', "The right click button is not pressed"

        def test_click_me(self, driver):
            web_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            web_page.open()
            click_result = web_page.simple_click()
            assert click_result == 'You have done a dynamic click', "The dynamic click button is not pressed"

    class TestLInks:
        def test_simple_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_link = links_page.check_simple_link()
            logger.info(href_link)
            assert href_link == current_link

        def test_dynamic_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_link = links_page.check_dynamic_link()
            logger.info(href_link)
            assert href_link == current_link

        def test_api_call_links(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            code_created, check_created = links_page.check_api_call_link('https://demoqa.com/created')
            logger.info([code_created, check_created])
            code_no_content, check_no_content = links_page.check_api_call_link('https://demoqa.com/no-content')
            code_moved, check_moved = links_page.check_api_call_link('https://demoqa.com/moved')
            code_bad_request, check_bad_request = links_page.check_api_call_link('https://demoqa.com/bad-request')
            code_unauthorized, check_unauthorized = links_page.check_api_call_link('https://demoqa.com/unauthorized')
            code_forbidden, check_forbidden = links_page.check_api_call_link('https://demoqa.com/forbidden')
            code_invalid_url, check_invalid_url = links_page.check_api_call_link('https://demoqa.com/invalid-url')
            assert code_created == check_created
            assert code_no_content == check_no_content
            assert code_moved == check_moved
            assert code_bad_request == check_bad_request
            assert code_unauthorized == check_unauthorized
            assert code_forbidden == check_forbidden
            assert code_invalid_url == check_invalid_url

    class TestUploadDownloadFile:

        def test_upload_file(self, driver):
            upload_ = UploadDownloadFilePage(driver, 'https://demoqa.com/upload-download')
            upload_.open()
            upload_name, uploaded_name = upload_.upload_file()
            assert upload_name == uploaded_name, "The file not upload"

        def test_download_file(self, driver):
            download_ = UploadDownloadFilePage(driver, 'https://demoqa.com/upload-download')
            download_.open()
            result = download_.download_file()
            assert result is True, "The file not download"

    class TestDynamicProperties:

        def test_enable_button(self, driver):
            enable_button = DynamicProperties(driver, 'https://demoqa.com/dynamic-properties')
            enable_button.open()
            enable_ = enable_button.check_enable_button()
            assert enable_ is True, "the button is invisible after 5 seconds"

        def test_change_color_button(self, driver):
            change_color_button = DynamicProperties(driver, 'https://demoqa.com/dynamic-properties')
            change_color_button.open()
            before_, after_ = change_color_button.check_change_color_button()
            assert before_ != after_, "the color not change"

        def test_visible_button(self, driver):
            visible_button = DynamicProperties(driver, 'https://demoqa.com/dynamic-properties')
            visible_button.open()
            visible_ = visible_button.check_visible_after_button()
            assert visible_ is True, "the button is invisible after 5 seconds"







