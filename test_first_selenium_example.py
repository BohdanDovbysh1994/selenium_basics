import time

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By


def test_01():
    chrome_driver = Chrome('chromedriver.exe')
    # chrome_driver.maximize_window()
    chrome_driver.get('https://admin-demo.nopcommerce.com')
    # time.sleep(5)
    actual_title = chrome_driver.title
    assert actual_title == 'Your store. Login'
    # chrome_driver.close()


def test_02():
    # Configgig file
    user_name = 'admin@yourstore.com'
    password = 'admin'
    # Fixtura
    chrome_driver = Chrome('chromedriver.exe')
    chrome_driver.maximize_window()
    chrome_driver.get('https://admin-demo.nopcommerce.com')

    # Page object
    email_input_locator = '//input[@id="Email"]'
    email_input_element = chrome_driver.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_name)

    # Page object
    password_input_locator = '#Password'
    password_input_element = chrome_driver.find_element(By.CSS_SELECTOR, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    password_input_element.send_keys(Keys.ENTER)
    # Page object
    login_button_locator = '//*[@type="submit"]'
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    logout_button_locator = "//div[@id='navbarText']//a[@href='/logout']"
    logout_button_element = chrome_driver.find_element(By.XPATH, logout_button_locator)
    is_logout_button = logout_button_element.is_displayed()

    assert is_logout_button is True, 'User was not logged-in'
    logout_button_element.screenshot('element_screenshot.jpg')
    chrome_driver.back()

    c = 0
