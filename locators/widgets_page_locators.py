from selenium.webdriver.common.by import By


class AccordionPageLocators:
    SECTION_1 = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_2 = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_3 = (By.CSS_SELECTOR, "div[id='section3Heading']")

    SECTION_1_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECTION_2_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    SECTION_3_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content'] p")


class AutoCompletePageLocators:
    MULTI_COMPLETE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
    MULTI_VALUE_TEXT = (By.CSS_SELECTOR, "div[id='autoCompleteMultipleContainer']")
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")
    MULTI_VALUE_REMOVE_ALL = (By.CSS_SELECTOR, "div[class='auto-complete__indicators css-1wy0on6'] svg path")
    SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
    SINGLE_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
