from framework.client.http_client import HttpClient
import pytest

class TestAuthFlows:

    @pytest.fixture
    def user_data(self):
        return {
            'username': 'emilys',
            'password': 'emilyspass'
        }

    @pytest.mark.api
    @pytest.mark.regression
    def test_auth_login(self, user_data, setup):
        headers = {'Content-type': 'application/json'}
        client = HttpClient()
        resp = client.post(path="/auth/login", json=user_data, headers=headers)

        assert resp.status_code == 200
