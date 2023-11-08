import requests
import json

class ErrorHandling:
    def __init__(self, endpoint):
        self.endpoint = endpoint


    def get_hold_of(self, **kwargs):
        try:
            response = requests.get(self.endpoint, params=kwargs)
            response.raise_for_status()
            return response
        # When using a wrong API key for the API endpoint of Alpha Vantage,
        # it currently returns still the status code 200.
        # The following workaround catches the wrong input as long as response.content contains the error message.
        except ConnectionError as c:
            print("An error occurred during your request: ", c)
            quit()
        except requests.exceptions.RequestException as e:
            if response.status_code == 200:
                result = response.content
                result_dic = json.loads(result)
                key = "Error Message"
                if key in result_dic:
                    print(f"Though the status code returned as {response.status_code}, an error got catched during your request:\nResponse content: {result_dic}")
                    quit()
            else:
                print(f"An error occurred during your request: {e}\nResponse content: {response.content}")
                quit()


