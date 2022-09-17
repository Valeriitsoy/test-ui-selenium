from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # FORM FIELDS ПОЛЯ ФОРМЫ

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # CREATED FORM Созданные формы

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_BUTTON = (By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[2]/label")
    NO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    OUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRSTNAME_FIL = (By.CSS_SELECTOR, "input[id='firstName']")
    LASTNAME_FIL = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_FIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_FIL = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_FIL = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_FIL = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    PERSON_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")

    SEARCH_FIL = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete'")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROWS = (By.CSS_SELECTOR, "select[aria-label='rows per page']")


class ButtonsLocators:
    DOUBLE_CLICK_ME = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    CHECK_DOUBLE_CLICK_ME = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")

    RIGHT_CLICK_ME = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CHECK_RIGHT_CLICK_ME = (By.CSS_SELECTOR, "p[id='rightClickMessage']")

    CLICK_ME = (By.XPATH, "//div[3]/button")    # динамический ID
    CHECK_CLICK_ME = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")


class LinksLocators:
    SIMPLE_LINk = (By.CSS_SELECTOR, "a[id='simpleLink']")
    DYNAMIC_LINK = (By.CSS_SELECTOR, "a[id='dynamicLink']")
    CREATED_LINK = (By.CSS_SELECTOR, "a[id='created']")
    NO_CONTENT_LINK = (By.CSS_SELECTOR, "a[id='no-content']")
    MOVED_LINK = (By.CSS_SELECTOR, "a[id='moved']")
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, "a[id='bad-request']")
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, "a[id='unauthorized']")
    FORBIDDEN_LINK = (By.CSS_SELECTOR, "a[id='forbidden']")
    NOT_FOUND_LINK = (By.CSS_SELECTOR, "a[id='invalid-url']")


class UploadDownloadFilePageLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOADED_RESULT = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")

    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id='downloadButton']")


class DynamicPropertiesLocators:
    ENABLE_BUTTON = (By.CSS_SELECTOR, "button[id='enableAfter']")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id='colorChange']")
    VISIBLE_AFTER_FIVE_S_BUTTON = (By.CSS_SELECTOR, "button[id='visibleAfter']")
