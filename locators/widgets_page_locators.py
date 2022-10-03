from selenium.webdriver.common.by import By


class AccordionPageLocators:
    SECTION_1 = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_2 = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_3 = (By.CSS_SELECTOR, "div[id='section3Heading']")

    SECTION_1_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECTION_2_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    SECTION_3_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content'] p")
