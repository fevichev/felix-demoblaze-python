import requests
from loguru import logger
from requests import HTTPError

from definitions import URL, HEADER_API
from rest.view_cart_api import get_product_id
from utils.helper import json_extract

uri = '/view'
base_server_url = URL.get('API')


def view_device_description_api(device_id):
    json_body = f'{{\"id\":\"{device_id}\"}}'

    try:
        response = requests.post(base_server_url + uri, data=json_body, headers=HEADER_API)
        response.raise_for_status()
    except HTTPError as http_err:
        logger.info(f'HTTP error occurred: {http_err}')
    else:
        logger.info('Way to go buddy! Your "view device description" request was sent successfully.')
    return response


def get_title(session):
    product_device_id = get_product_id(session)
    return json_extract(view_device_description_api(product_device_id).json(), 'title')[0]


def get_price(session):
    product_device_id = get_product_id(session)
    return json_extract(view_device_description_api(product_device_id).json(), 'price')[0]
