import time

from pages.alerts_win_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, ModalDialogsPage


class TestAlertsWin:

    class TestWindows:

        def test_new_simple_windows(self, driver):
            new_tab = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab.open()
            result_ = new_tab.check_opened_new('tab')
            assert result_ == 'This is a sample page'

    class TestAlertsButtons:

        def test_to_see_alert(self, driver):
            alert_ = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_.open()
            alert_text = alert_.check_see_alert()
            assert alert_text == 'You clicked a button'

        def test_five_seconds_alert(self, driver):
            alert_ = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_.open()
            alert_text = alert_.check_five_seconds_alert()
            assert alert_text == 'This alert appeared after 5 seconds'

        def test_confirm_box_alert(self, driver):
            alert_ = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_.open()
            alert_text = alert_.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        def test_dismiss_box_alert(self, driver):
            alert_ = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_.open()
            alert_text = alert_.check_dismiss_alert()
            assert alert_text == 'You selected Cancel'

        def test_prompt_alert(self, driver):
            alert_ = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_.open()
            text, alert_text = alert_.check_prompt_alert()
            assert text in alert_text

    class TestFramesPage:

        def test_frames(self, driver):
            frame_ = FramesPage(driver, 'https://demoqa.com/frames')
            frame_.open()
            result_1 = frame_.check_frame('frame1')
            result_2 = frame_.check_frame('frame2')
            assert result_1 == ['This is a sample page', '500px', '350px'], "The frame not found"
            assert result_2 == ['This is a sample page', '100px', '100px'], "The frame not found"

    class TestNestedFramesPage:

        def test_nested_frames(self, driver):
            nested_frame = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame.open()
            parent_text, child_text = nested_frame.check_nested_frame()
            assert parent_text == 'Parent frame', "The frame is not created"
            assert child_text == 'Child Iframe', "The iframe is not created"

    class TestModalDialogsPage:

        def test_modal_dialog(self, driver):
            modal_dialog = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog.open()
            s_title, l_title = modal_dialog.check_modal_dialog()
            assert s_title == "Small Modal"
            assert l_title == "Large Modal"
