import requests
from requests import HTTPError

from definitions import URL
from rest.login_api import get_auth_token_api
from utils.helper import json_extract

uri = '/viewcart'
base_server_url = URL.get('API')


def view_cart_via_api(session):
    authentication_token = get_auth_token_api(session)
    json_body = '{\"cookie\": \"' + authentication_token + '\",\"flag\": true}'
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(base_server_url + uri, data=json_body, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        print('Way to go buddy! Your "view cart" request was sent successfully.')
    return response


def get_size_of_items_in_cart(session):
    return len(view_cart_via_api(session).json()['Items'])


def get_product_id(session):
    return json_extract(view_cart_via_api(session).json(), 'prod_id')[0]
