import requests


class Proxy:
    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        object_instance = self.instance
        if object_instance.numero % 2 == 0:
            continente = "asia"
            response = requests.get(f"https://restcountries.eu/rest/v2/region/{continente}")
            print(
                response.content
            )
        else:
            continente = "europe"
            response = requests.get(f"https://restcountries.eu/rest/v2/region/{continente}")
            print(
                response.content
            )
        return False
