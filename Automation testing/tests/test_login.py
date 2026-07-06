import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

email = "dharsanagopal1@gmail.com"       
password = "Dharsh@29" 


def test_valid_login(driver):
    login = LoginPage(driver)
    login.login(email, password)
    WebDriverWait(driver, 10).until(EC.url_contains("home"))
    assert "home" in driver.current_url


def test_invalid_email1(driver):
    login = LoginPage(driver)
    login.enter_email("abc")
    login.click_continue()
    time.sleep(2)
    assert "home" not in driver.current_url


def test_invalid_email2(driver):
    login = LoginPage(driver)
    login.enter_email("abc@")
    login.click_continue()
    time.sleep(2)
    assert "home" not in driver.current_url


def test_invalid_email3(driver):
    login = LoginPage(driver)
    login.enter_email("abc@gmail")
    login.click_continue()
    time.sleep(2)
    assert "home" not in driver.current_url


def test_invalid_email4(driver):
    login = LoginPage(driver)
    login.enter_email("@gmail.com")
    login.click_continue()
    time.sleep(2)
    assert "home" not in driver.current_url


def test_invalid_email5(driver):
    login = LoginPage(driver)
    login.enter_email("abc.com")
    login.click_continue()
    time.sleep(2)
    assert "home" not in driver.current_url


def test_email_empty(driver):
    login = LoginPage(driver)
    login.click_continue()
    time.sleep(2)
    assert "home" not in driver.current_url

def test_both_empty(driver):
    login = LoginPage(driver)
    login.click_continue()
    time.sleep(2)
    assert "home" not in driver.current_url


def test_password_mask(driver):
    login = LoginPage(driver)
    login.enter_email(email)
    login.click_continue()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    login.enter_password("test123")
    assert login.is_password_masked()



def test_page_title(driver):
    assert "Tichi" in driver.title


def test_login_url(driver):
    assert "login" in driver.current_url