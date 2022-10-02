from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_WINDOW_MESSAGE_BUTTON = (By.CSS_SELECTOR, "button[id='messageWindowButton']")

    TITLE_NEW = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    TEXT_NEW = (By.XPATH, "/html/body/text()")


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    ALERT_FIVE_SECONDS_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    PROMPT_BOX_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")

    CONFIRM_RESULT_TEXT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_RESULT_TEXT = (By.CSS_SELECTOR, "span[id='promptResult']")


class FramesPageLocators:
    FRAME_ONE = (By.CSS_SELECTOR, "iframe[id='frame1']")
    FRAME_TWO = (By.CSS_SELECTOR, "iframe[id='frame2']")

    TITLE_FRAME = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")

    PARENT_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_TEXT = (By.CSS_SELECTOR, "p")


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")

    SMALL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    LARGE_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeLargeModal']")

    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")



