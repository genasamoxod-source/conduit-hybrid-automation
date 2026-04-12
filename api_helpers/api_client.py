import os
import requests
from dotenv import load_dotenv


load_dotenv()


class ApiClient:
    def __init__(self):
        self.base_url =os.getenv('API_URL')
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
    
    def post(self,endpoint,data=None):
        url = f'{self.base_url}{endpoint}'
        response = self.session.post(url,json=data)
        return response
    
    def get(self,endpoint,params=None):
        url = f'{self.base_url}{endpoint}'
        return self.session.get(url, params=params)