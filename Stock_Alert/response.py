import requests


class Response:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get_hold_of(self, **kwargs):
        try:
            response = requests.get(self.endpoint, params=kwargs)
            response.raise_for_status()
            return response
        except ValueError as v:
            print(v, ": Please provide a valid API key and try again.")
        except ConnectionError as c:
            print("An error occurred: ", c)
        except requests.exceptions.RequestException as e:
            print("An error occurred during your request:", e)




