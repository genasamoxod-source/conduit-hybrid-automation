from api_helpers.api_client import ApiClient



class ArticlesHelper(ApiClient):
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