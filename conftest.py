from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.common.by import By
import creds

SIGNIN_PAGE = 'https://www.mynetdiary.com/logonPage.do'


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def auth(driver):
    driver.get(SIGNIN_PAGE)
    login = driver.find_element(By.ID, 'username-or-email')
    password = driver.find_element(By.ID, 'password')
    login.send_keys(creds.email)
    password.send_keys(creds.password)
    signin_button = driver.find_element(By.XPATH, '//span[@class="MuiButton-label-154 jss14"]')
    signin_button.click()
