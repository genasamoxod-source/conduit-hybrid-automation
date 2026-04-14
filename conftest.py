import pytest
import os
from api_helpers.auth_helper import AuthHelper
from api_helpers.create_arc_helper import ArticlesHelper
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

@pytest.fixture(scope="session")
def auth_token():
    """Фикстура для логина и получения токена"""
    auth = AuthHelper()
    email = os.getenv("USER_EMAIL")
    password = os.getenv("USER_PASSWORD")
    
    token = auth.login(email, password)
    return token


@pytest.fixture
def browser_logged_in(auth_token):
    path = r"C:\Users\genas\.wdm\drivers\geckodriver\win64\v0.36.0\geckodriver.exe"
    service = Service(executable_path=path)
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Firefox(service=service, options = options)
    driver.get(os.getenv('BASE_URL')) # Сначала заходим на сайт
    
    # "Вшиваем" токен в память браузера (localStorage)
    # Большинство современных сайтов (как Conduit) хранят токен там
    script = f"window.localStorage.setItem('id_token', '{auth_token}');"
    driver.execute_script(script)
    
    # Обновляем страницу — и вуаля, ты залогинен!
    driver.refresh()
    
    yield driver
    driver.quit()