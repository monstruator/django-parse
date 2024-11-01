from django.db import models
import json


class UserCredentials(models.Model):
    username = models.CharField("Username", max_length=64, unique=True)
    password = models.CharField("Pass", max_length=64)
    cookies = models.TextField("Cookies", blank=True, null=True)

    def set_cookies(self, cookies_dict):
        self.cookies = json.dumps(cookies_dict)

    def get_cookies(self):
        return json.loads(self.cookies)

    def __str__(self):
        return self.username
