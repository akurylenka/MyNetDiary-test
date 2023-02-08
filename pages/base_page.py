from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def text_to_be_present(self, locator, value):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, value))

    def visibility_of_all_elements(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))

    def find_all(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def find_new_value(self, locator, value):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value(locator, value))
        return self.driver.find_element(*locator)

    def text_is_present(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    def click(self, locator):
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()

    def send_keys(self, locator, value):
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
        element.send_keys(value)

    def is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def no_locator(self, locator):
        return WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(locator))

    def no_value_in_locator(self, locator, text):
        return WebDriverWait(self.driver, 10).until_not(EC.text_to_be_present_in_element_value(locator, text))

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
