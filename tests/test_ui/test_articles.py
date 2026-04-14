from api_helpers.create_arc_helper import CreateArc
import time

def test_create_article_visible_in_profile(browser_logged_in,auth_token):


    title = f'Test Article {time.time()}'


    api = CreateArc()
    api.session.headers.update({"Authorization": f"Token {auth_token}"})
    slug = api.post('/articles',data={'article':{'title':title,'descripton':'desc','body':'text'}}).json()["article"]["slug"]

    browser_logged_in.refresh()


    print(f"Статья '{title}' создана и проверена!")

    api.delete(slug)

    print('Артикль удален!')


