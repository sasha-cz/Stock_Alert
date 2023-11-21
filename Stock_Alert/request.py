import requests


class Request:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def make(self, params):
        response = requests.get(self.endpoint, params)
        response.raise_for_status()
        return response
