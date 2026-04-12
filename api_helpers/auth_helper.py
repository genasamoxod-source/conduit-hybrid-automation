from api_helpers.api_client import ApiClient


class AuthHelper(ApiClient):
    def login(self,email,password):
        payload = {'user':{
        'email' : email,
        'password': password
        }
    }
        response = self.post('/users/login',data=payload)

        if response.status_code == 200:
            token = response.json()['user']['token']
            self.session.headers.update({"Authorization": f"Token {token}"})
            return token
        else:
            raise Exception(f"Login failed: {response.status_code}, {response.text}")