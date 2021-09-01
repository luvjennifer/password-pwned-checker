import requests


class NetworkInterface():
    def __init__(self):
        pass

    def get(self, url, param):
        response = requests.get(url + param)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print(error)
            raise RuntimeError('network error') from exc
        else:
            return response
