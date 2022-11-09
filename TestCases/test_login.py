# import time
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
from PageObjects.LoginPage import login
from PageObjects.Dashboard import Database
from selenium import webdriver


@pytest.mark.usefixtures("setup")
class BaseTest:
    pass


class Test_login(BaseTest):
    def test_validCredential(self):
        lg=login(self.driver)
        db = Database(self.driver)
        lg.input_username("Admin")
        lg.input_password("admin123")
        lg.click_login()

        if "Dashboard" in db.dashboardmsg():
            assert True
        else:
            assert False
    def test_InvalidePassword(self):
        lg = login(self.driver)
        lg.input_username("Admin")
        lg.input_password("admin125")
        lg.click_login()
        if "Invalid credentials" in lg.invalide_Text():
            assert True
        else:
            assert False
    def test_InvalideUsername(self):
        lg = login(self.driver)
        lg.input_username("jaya")
        lg.input_password("admin123")
        lg.click_login()

        if "Invalid credentials" in lg.invalide_Text():
            assert True
        else:
            assert False




# time.sleep(2)
# driver.find_element(By.XPATH,"//span[text()='Admin']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//span[text()='Job ']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//a[text()='Employment Status']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
# time.sleep(4)
#
# driver.find_element(By.XPATH, "//label[text()='Name']").send_keys("pytest_Framework")
# #add_proName.send_keys("pytest_Framework")
# time.sleep(8)
# #driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click()



