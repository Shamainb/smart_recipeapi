from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
import json

'''
Handles form errors that are passed back to AJAX calls
'''
def FormErrors(*args):
    message = ""
    for f in args:
        if f.errors:
            message = f.errors.as_text()
    return message

'''
Used to append URL parameters when redirecting users
'''
def RedirectParams(**kwargs):
    url = kwargs.get("url")
    params = kwargs.get("params")
    response = redirect(url)
    if params:
        query_string = urlencode(params)
        response['Location'] += '?' + query_string
    return response

class APIMixin:
    def __init__(self, *args, **kwargs):
        self.query = kwargs.get("query")
        self.cat = kwargs.get("cat")
        self.id = kwargs.get("id")

    def get_data(self):
        url_dict = {
            "recipes": "recipes/complexSearch?",
            "ingredients": "food/ingredients/search?",
            "menuItems": "food/menuItems/search?",
            "products": "food/products/search?"
        }

        url = f"https://api.spoonacular.com/{url_dict[self.cat]}query={self.query}&apiKey={settings.API_KEY}"

        r = requests.get(url)
        if r.status_code == 200:
            try:
                return r.json()[self.cat]
            except KeyError:
                return r.json()['results']
        else:
            return None

    def get_detail_data(self):
        url_dict = {
            "recipes": f"recipes/{self.id}/information?",
            "ingredients": f"food/ingredients/{self.id}/information?",
            "menuItems": f"food/menuItems/{self.id}?",
            "products": f"food/products/{self.id}?"
        }

        if self.cat in url_dict:
            url = f"https://api.spoonacular.com/{url_dict[self.cat]}apiKey={settings.API_KEY}"
            r = requests.get(url)
            if r.status_code == 200:
                return r.json()
            else:
                return None
