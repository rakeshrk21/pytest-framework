"""
requests
├── Session class
├── Response class
├── get()
├── post()
├── put()
└── delete()

"""
import requests
from requests import Response

from framework.config.settings import BASE_URL

class HttpClient:
    def __init__(self, timeout=10):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.timeout = timeout

    def get(self, path: str, **kwargs) -> Response:
        return self._request(method="GET", path=path, **kwargs)

    def post(self, path: str, json: dict, **kwargs) -> Response:
        return self._request(method="POST", path=path, json=json, **kwargs)

    def _request(
        self,
        method: str,
        path: str,
        json: dict | None = None,
        **kwargs,
    ) -> Response:
        return self.session.request(
            method=method,
            url=self.base_url + path,
            timeout=self.timeout,
            json=json,
            **kwargs
        )
