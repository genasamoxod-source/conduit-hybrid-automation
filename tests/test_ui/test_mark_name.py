from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import time

def test_user_is_logged_in(browser_logged_in):
    wait = WebDriverWait(browser_logged_in,10)
    profile_link = wait.until(ES.visibility_of_element_located((By.XPATH, '//a[@href="/@valerick/"]')))
    assert profile_link.is_displayed()
    print(f"Успешно залогинены под: {profile_link.text}")