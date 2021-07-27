import requests

from common.requests import Requests
from common.deco import logging as log


class Client(Requests):
    def __init__(self, url):
        self.url = url

    s = requests.Session()

    USERS = "/users"

    @log("Get Users")
    def get_users(self, data, type_response=None):
        res = self.s.get(self.url + f"/{self.USERS}")
        return self.structure(res, type_response=type_response)

    @log("Get Users by id")
    def get_users_id(self, data, type_response=None, id_user=0):
        res = self.s.get(self.url + f"/{self.USERS}" f"/{id_user}")
        return self.structure(res, type_response=type_response)

    @log("Post User")
    def post_users(self, data, type_response=None):
        res = self.s.post(self.url + f"/{self.USERS}", json=data.__dict__)
        return self.structure(res, type_response=type_response)

    @log("Delete Users by id in body")
    def delete_users(self, data, type_response=None):
        res = self.s.delete(self.url + f"/{self.USERS}", json=data.__dict__)
        return self.structure(res, type_response=type_response)

    @log("Delete Users by id")
    def delete_users_id(self, data, type_response=None, id_user=3):
        res = self.s.delete(self.url + f"/{self.USERS}" f"/{id_user}")
        return self.structure(res, type_response=type_response)
