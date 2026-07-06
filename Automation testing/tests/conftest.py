import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://tichi-app-webapp-stage.web.app/login")
    driver.maximize_window()
    yield driver
    driver.quit()