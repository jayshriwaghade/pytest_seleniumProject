from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage


class login(BasePage):
    def __init__(self,driver):
        self.driver=driver

        self.textbox_username_xpath="//input[@name='username']"
        self.textbox_password_xpath="//input[@name='password']"
        self.button_login_xpath    ="//button[text()=' Login ']"
        self.text_invalidemsg_xpath="//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"
    def input_username(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)
    def input_password(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
    def invalide_Text(self):
        return self.driver.find_element(By.XPATH, self.text_invalidemsg_xpath).text


