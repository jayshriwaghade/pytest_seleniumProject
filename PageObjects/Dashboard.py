from selenium.webdriver.common.by import By


class Database():
    def __init__(self,driver):
        self.driver=driver

        self.text_dashboardemsg_xpath="//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"
    def dashboardmsg(self):
        return self.driver.find_element(By.XPATH,self.text_dashboardemsg_xpath).text