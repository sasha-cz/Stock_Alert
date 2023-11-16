import requests


class Request:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def make(self, params):
        try:
            response = requests.get(self.endpoint, params)
            response.raise_for_status()
            return response
        except ConnectionError as c:
            raise Exception("An error occurred during your request: ", c)
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred during your request: {e}\nResponse: {response.content}")
