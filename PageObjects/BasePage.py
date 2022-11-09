from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
"""" This class is the parent of all pages"""
"""It contains all the generic methods and utilities for all pages"""
class BasePage:
    def __init__(self,driver):
        self.driver=driver
    """this method is used to get the title of application"""

    def get_title(self,title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title
    """this method is used to click on webElement"""
    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    """this method is used to send the test"""
    def do_send_keys(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located()).send_keys(text)

    """This method is used to get the text of particular WebElement"""

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """This method is used to whether WebElement is Visible or Not"""

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)