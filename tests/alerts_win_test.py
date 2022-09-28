from pages.alerts_win_page import BrowserWindowsPage


class TestAlertsWin:

    class TestWindows:

        def test_new_simple_windows(self, driver):
            new_tab = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab.open()
            result_ = new_tab.check_opened_new('tab')
            assert result_ == 'This is a sample page'
