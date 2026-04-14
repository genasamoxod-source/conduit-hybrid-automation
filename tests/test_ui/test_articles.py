from api_helpers.create_arc_helper import ArticlesHelper
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.by import By

def test_create_article_visible_in_profile(browser_logged_in,auth_token):

    print(f"Создание статье через API")
    wait= WebDriverWait(browser_logged_in,10)

    title = f'Test Article {time.time()}'

    api = ArticlesHelper()
    api.session.headers.update({"Authorization": f"Token {auth_token}"})
    slug = api.post('/articles',data={'article':{'title':title,'descripton':'desc','body':'text'}}).json()["article"]["slug"]

    browser_logged_in.refresh()

    wait.until(ES.visibility_of_element_located((By.XPATH,f'//div[@class="article-preview"]/a[@class="preview-link"]/h1[text()="{title}"]')))
    print(f"Статья '{title}' создана и проверена!")

    response = api.delete("/articles/",slug)
    assert response.status_code < 300 and response.status_code >= 200
    print(f"Статья '{title}' удалена!")

    print('Артикль удален!')


