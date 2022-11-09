import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
@pytest.fixture
def setup(request):
    service_obj = Service("C:/Users/LENOVO/PycharmProjects/Drivers/chromedriver_win32 (1)/chromedriver.exe")
    request.cls.driver = webdriver.Chrome(service=service_obj)
    request.cls.driver.implicitly_wait(5)
    #request.cls.driver=webdriver.Chrome(executable_path="C:/Users/LENOVO/PycharmProjects/Drivers/chromedriver_win32 (1)/chromedriver.exe")
    request.cls.driver.get("https://opensource-demo.orangehrmlive.com")
    request.cls.driver.implicitly_wait(5)
    yield
    request.cls.driver.quit()

    #service_obj = Service("C:/Users/LENOVO/PycharmProjects/Drivers/chromedriver_win32 (1)/chromedriver.exe")
    #driver = webdriver.Chrome(service=service_obj)
    # driver.maximize_window()
    # driver.implicitly_wait(9)
    # request.cls.driver.get("https://opensource-demo.orangehrmlive.com")
    #
    # return driver
