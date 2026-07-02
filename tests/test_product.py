import pytest
from framework.client.http_client import HttpClient

class TestProduct:

    @pytest.fixture
    def client(self):
        return HttpClient()

    @pytest.mark.api
    def test_get_product(self, client):
        response = client.get('/products/2')
        json = response.json()
        print(json)

        assert json['title']=='Eyeshadow Palette with Mirror'
        assert json['price']==19.99
        assert json['discountPercentage']==18.19
        assert json['rating']==2.86

"""
Server
   │
   │ HTTP Response
   ▼
'{
    "id":2,
    "title":"Eyeshadow"
}'
        │
        │ response.text
        ▼
Python String
        │
        │ json.loads()
        ▼
Python Dictionary
        │
        │ response.json()
        ▼
{
    "id":2,
    "title":"Eyeshadow"
}
"""