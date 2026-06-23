from framework.client.http_client import HttpClient
from framework.utils.logger import get_logger


class TestCarts:

    def setup_method(self):
        self.client = HttpClient()
        self.log = get_logger('TestCarts')

    def test_user_can_get_all_items_available_in_cart(self):

        response = self.client.get(path='/carts')

        assert response.status_code == 200
        assert response.json()["carts"]


    def test_user_can_get_a_specific_item_from_the_cart(self):
        response = self.client.get(path='/carts/1')

        assert response.status_code == 200
        assert response.json()["products"]
        self.log.info(response.json()["products"])

