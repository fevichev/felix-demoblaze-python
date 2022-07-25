import requests
from requests import HTTPError

from definitions import URL

uri = '/deletecart'
baseServerUrl = URL.get('API')


def delete_cart_via_api(username):
    json_body = '{\"cookie\": \"' + username + '\"}'
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(baseServerUrl + uri, data=json_body, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        print('Success!')
