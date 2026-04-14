from api_helpers.api_client import ApiClient



class CreateArc(ApiClient):
    def creare_arcticle(self,title,description,body):
        payload = {
            'article':{
                'title': title,
                'description':description,
                "body": body,
                'taglist':[]
            }
        }
        return self.post('/articles',data=payload)
    
    def delete(self,slug):
        self.session.delete(f"{self.base_url}/articles/{slug}")